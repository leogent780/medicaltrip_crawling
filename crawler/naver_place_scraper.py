"""네이버 검색결과(플레이스 탭)와 플레이스 상세를 순수 HTTP 요청으로 조회하는 크롤러.

Playwright 같은 브라우저 자동화 없이 requests로만 동작한다. 지도 화면(map.naver.com)을
직접 열고 클릭하는 방식보다 "자동화 브라우저" 신호가 훨씬 적어서 캡차가 덜 뜬다
(피부과 업체 수집 때 이 방식으로 성공한 사례 기반).

주의:
- search.naver.com 검색결과 페이지에 내장된 JSON을 정규식으로 그대로 뽑는 방식이라
  공식 계약이 아니다. 네이버가 마크업/필드 구성을 바꾸면 깨질 수 있다.
- map.naver.com/p/api/place/summary, m.place.naver.com/place/* 도 마찬가지로 비공식
  내부 엔드포인트라 언제든 바뀔 수 있다.
- 개인 리서치용 소규모 수집을 전제로 만들었다. SEARCH_DELAY/DETAIL_DELAY를 임의로
  줄이지 말 것.
"""

import argparse
import re
import time
from dataclasses import dataclass

import requests
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

SEARCH_DELAY = 1.0
DETAIL_DELAY = 0.5

REGION_ALIASES = {
    "명동": ["명동", "을지로입구", "충무로"],
    "성수": ["성수", "성수동", "뚝섬"],
    "홍대": ["홍대", "연남동", "합정"],
    "강남": ["강남역", "역삼동", "논현동"],
    "압구정": ["압구정", "압구정로데오"],
    "신사": ["신사동", "가로수길"],
    "용산": ["용산", "이태원", "한남동"],
}

INSTAGRAM_PATTERNS = [
    re.compile(r"instagram\.com/([A-Za-z0-9._]{2,30})"),
    re.compile(r'"instagram"\s*:\s*"([^"]+)"'),
    re.compile(r'instaId["\s:]+([A-Za-z0-9._]{2,30})'),
]
KAKAO_RE = re.compile(r"pf\.kakao\.com/[A-Za-z0-9_]+")
TAG_RE = re.compile(r"<[^>]+>")
IGNORE_INSTA_HANDLES = {"p", "reel", "explore", "stories", "accounts", ""}


def make_session():
    session = requests.Session()
    session.headers.update({
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"),
        "Accept-Language": "ko-KR,ko;q=0.9",
    })
    return session


@dataclass
class Place:
    id: str
    region: str
    name: str = ""
    address: str = ""
    phone: str = ""
    instagram: str = ""
    kakao_channel: str = ""
    first_visit_event: str = ""


def build_queries(region, keyword):
    aliases = REGION_ALIASES.get(region, [region])
    return [f"서울 {alias} {keyword}" for alias in aliases]


def search_places(session, query, region, log=print):
    places = []
    url = "https://search.naver.com/search.naver"
    params = {"where": "place", "query": query, "display": 70}
    try:
        resp = session.get(url, params=params, timeout=15)
        text = resp.text
        ids = re.findall(r'"id"\s*:\s*"(\d{7,})"', text)
        names = re.findall(r'"name"\s*:\s*"([^"]{2,30})"', text)
        addresses = re.findall(r'"roadAddress"\s*:\s*"([^"]*)"', text)
        phones = re.findall(r'"phone"\s*:\s*"([^"]*)"', text)
        for i, pid in enumerate(ids):
            places.append(Place(
                id=pid,
                region=region,
                name=names[i] if i < len(names) else "",
                address=addresses[i] if i < len(addresses) else "",
                phone=phones[i] if i < len(phones) else "",
            ))
    except requests.RequestException as e:
        log(f"  [오류] '{query}' 검색 실패: {e}")
    return places


def enrich_place(session, place, log=print):
    detail_urls = [
        f"https://map.naver.com/p/api/place/summary/{place.id}",
        f"https://m.place.naver.com/place/{place.id}/home",
    ]
    combined_text = ""
    for url in detail_urls:
        try:
            resp = session.get(url, timeout=10)
            combined_text += resp.text
        except requests.RequestException:
            continue

    for pattern in INSTAGRAM_PATTERNS:
        m = pattern.search(combined_text)
        if m:
            handle = m.group(1).strip("/").strip('"')
            if handle.lower() not in IGNORE_INSTA_HANDLES:
                place.instagram = f"https://www.instagram.com/{handle}/"
                break

    m = KAKAO_RE.search(combined_text)
    if m:
        place.kakao_channel = m.group(0)

    try:
        resp = session.get(f"https://m.place.naver.com/place/{place.id}/feed", timeout=10)
        idx = resp.text.find("첫방문")
        if idx != -1:
            start = resp.text.rfind(" ", 0, max(0, idx - 15)) + 1
            snippet = TAG_RE.sub(" ", resp.text[start: idx + 60])
            place.first_visit_event = snippet.strip()
    except requests.RequestException:
        pass

    return place


def crawl(regions, keyword, max_per_region, log=print):
    session = make_session()
    all_places = {}

    for region in regions:
        log(f"[INFO] === {region} 검색 시작 ===")
        for query in build_queries(region, keyword):
            log(f"[INFO] 검색: {query}")
            found = search_places(session, query, region, log=log)
            new = 0
            for p in found:
                if p.id not in all_places:
                    all_places[p.id] = p
                    new += 1
            region_count = sum(1 for x in all_places.values() if x.region == region)
            log(f"  -> {new}개 신규 (지역 누적 {region_count}개)")
            time.sleep(SEARCH_DELAY)
            if region_count >= max_per_region:
                break

    log(f"\n[INFO] 총 {len(all_places)}곳 발견. 상세정보(인스타/카톡/첫방문이벤트) 조회 중...")
    for place in all_places.values():
        enrich_place(session, place, log=log)
        log(f"    - {place.name} | {place.address} | IG:{place.instagram or '-'}")
        time.sleep(DETAIL_DELAY)

    return list(all_places.values())


def save_excel(places, output_path, log=print):
    wb = Workbook()
    ws = wb.active
    ws.title = "에스테틱 리스트"
    headers = ["지역", "업체명", "주소", "전화번호", "인스타그램",
               "카카오톡채널", "첫방문이벤트", "네이버플레이스ID"]
    ws.append(headers)

    seen = set()
    for p in places:
        key = (p.name, p.address)
        if key in seen:
            continue
        seen.add(key)
        ws.append([p.region, p.name, p.address, p.phone, p.instagram,
                   p.kakao_channel, p.first_visit_event, p.id])

    for i, h in enumerate(headers, start=1):
        ws.column_dimensions[get_column_letter(i)].width = max(14, len(h) + 4)

    wb.save(output_path)
    log(f"[INFO] 엑셀 저장 완료: {output_path} (총 {len(seen)}곳)")


def main():
    parser = argparse.ArgumentParser(description="네이버 검색/플레이스 HTTP 기반 에스테틱 크롤러")
    parser.add_argument("--regions", nargs="+",
                         default=["명동", "성수", "홍대", "강남", "압구정", "신사", "용산"])
    parser.add_argument("--keyword", default="에스테틱")
    parser.add_argument("--max-per-region", type=int, default=15)
    parser.add_argument("--output", default="seoul_esthetic_list.xlsx")
    args = parser.parse_args()

    places = crawl(args.regions, args.keyword, args.max_per_region)
    save_excel(places, args.output)


if __name__ == "__main__":
    main()
