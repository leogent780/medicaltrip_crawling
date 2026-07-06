# 서울 에스테틱 크롤러

지역명 + 키워드(기본 "에스테틱")로 업체를 찾아서 주소/전화번호/인스타그램/카카오톡채널/
첫방문이벤트를 모아 엑셀로 저장한다. 세 가지 방식이 있다.

| | `naver_place_scraper.py` (기본/추천) | `naver_api_crawler.py` | `naver_esthetic_crawler.py` |
|---|---|---|---|
| 방식 | 검색결과+플레이스 페이지를 순수 HTTP 요청으로 조회 | 네이버 공식 오픈 API | 네이버 지도 화면 직접 자동화 (Playwright) |
| 캡차 | 거의 안 뜸 | 없음 | 뜰 수 있음 |
| API 키 | 불필요 | 필요 (무료 발급) | 불필요 |
| 데이터 소스 | 비공식 내부 엔드포인트 (구조 바뀌면 깨질 수 있음) | 공식 계약 (지역검색 쿼리당 5건 제한) | 실제 화면에 보이는 그대로 |

`webapp.py`는 기본적으로 **`naver_place_scraper.py`**를 사용한다. 이게 안 되거나 막히면
`naver_api_crawler.py`(공식 API, 키 발급 필요)로 바꿔서 써도 된다.

## 1. 기본 방식: naver_place_scraper.py (API 키 불필요)

```bash
cd crawler
pip install -r requirements.txt
python naver_place_scraper.py --regions 명동 성수 홍대 강남 압구정 신사 용산 \
  --keywords 에스테틱 스파 마사지 헤어 메이크업 --max-per-region 15
```
`--keywords`에 여러 개를 주면 지역 x 키워드 조합마다 각각 검색하고, 여러 키워드에
겹치는 업체는 하나로 합쳐서 "검색키워드" 칸에 어떤 키워드로 잡혔는지 모아서 보여준다.

### 웹 화면으로 실행
```bash
python webapp.py
```
브라우저에서 `http://127.0.0.1:5000` 접속 → 지역 체크박스 선택, 키워드 칸에 콤마로
여러 개 입력(예: `에스테틱, 스파, 마사지, 헤어, 메이크업`), 개수 입력 → "크롤링 시작"
클릭. 진행 로그가 화면에 쌓이다가 끝나면 "엑셀 다운로드" 버튼이 뜬다.

### 알아둘 점
- `search.naver.com`의 플레이스 검색결과 페이지에 내장된 JSON을 정규식으로 그대로
  뽑는 방식이다. 공식 API가 아니라서 네이버가 마크업/필드 구성을 바꾸면 깨질 수 있다.
  그런 경우 알려주면 정규식을 다시 맞춰줄 수 있다.
- 검색 한 번에 미리보기 몇 개(보통 7~8개)만 오는 것 같아서, `start` 파라미터로 다음
  페이지를 최대 `MAX_SEARCH_PAGES`(기본 5)번까지 더 요청해서 합친다. 새 업체가 하나도
  안 나오는 페이지가 나오면 거기서 멈춘다. `--debug`로 돌리면 `search_..._p1.html`,
  `_p2.html`처럼 페이지별 원본이 남아서, 실제로 페이지가 늘어나며 다른 업체가 나오는지
  확인할 수 있다.
- 인스타그램/카카오톡채널은 먼저 `map.naver.com/p/api/place/summary/{id}`,
  `m.place.naver.com/place/{id}/home`(업체가 네이버 플레이스에 직접 등록해둔 정보)에서
  찾고, 못 찾으면 **업체명으로 블로그 후기를 검색**해서 "@계정명" 언급을 보조로 찾는다.
  블로그에도 언급이 없으면 그때는 정말로 빈 칸으로 남는다 — 없는 걸 지어내지 않는다.
  (소규모 업체는 플레이스에 SNS를 안 채워둔 경우가 많아서 블로그 보조검색 비중이 크다.)
- 첫방문 이벤트도 `m.place.naver.com/place/{id}/feed`(소식탭) → 안 나오면 블로그 후기
  순서로 "첫방문" 문구를 찾는다.
- `--debug`를 켜면 업체별로 상세/피드/블로그 원문 응답을 `debug/` 폴더에 저장한다.
  인스타가 이상하게 안 잡히거나 잘못 잡히면 이 폴더 내용을 공유해주면 정규식을 맞게
  고칠 수 있다.
- `SEARCH_DELAY`(검색 사이 1초), `DETAIL_DELAY`(상세조회 사이 0.5초)를 임의로 줄이지
  말 것. 그래도 캡차가 자주 뜨면 `--max-per-region`을 줄이고 지역 수를 나눠서 여러
  번에 걸쳐 돌리는 걸 추천.

## 2. 대안: naver_api_crawler.py (네이버 공식 오픈 API)

캡차 위험을 완전히 없애고 싶으면 이 방식을 쓴다. 다만 API 키 발급이 필요하고, 지역검색
API가 쿼리당 5건 제한이라 커버리지가 좀 더 좁다.

1. https://developers.naver.com/apps → 애플리케이션 등록 → 사용 API에서 "검색" 체크
2. 발급받은 Client ID/Secret을 `crawler/.env`에 저장 (`.env.example` 참고)
3. 실행:
   ```bash
   python naver_api_crawler.py --regions 명동 성수 홍대 --max-per-region 15
   ```
4. `webapp.py`에서 이 방식을 쓰고 싶으면 `from naver_place_scraper import ...`를
   `from naver_api_crawler import ...`로 바꾸면 된다.

## 3. 대안: naver_esthetic_crawler.py (브라우저 자동화, 캡차 위험)

네이버 지도 화면을 Playwright로 직접 열어서 훑는 방식. 위 두 방식으로 안 되는 정보를
보완하고 싶을 때만 보조적으로 사용 권장.

```bash
playwright install chromium
python naver_esthetic_crawler.py --regions 명동 --max-per-region 15
```
- `--headless`: 브라우저 창 숨김 (기본은 창을 띄움 — 캡차 뜨면 직접 풀어주기 편해서)
- `--debug`: 단계별 스크린샷을 `debug/`에 저장

## 공통 주의사항
- 개인적인 리서치 목적의 소규모 수집을 전제로 만들었다. 대량/상업적 재판매 용도로 쓰지
  말 것. 탐지 우회 전용 도구(undetected-chromedriver 등)는 의도적으로 넣지 않았다.
- 이 코드는 실제 네이버 서버에 접속해 테스트하지 못한 상태로 작성됐다(작업 환경 네트워크
  정책상 외부 접속이 막혀 있었음). 로직은 가짜 응답으로 단위 테스트했지만, 실제 응답
  형식과 다를 수 있다. 로컬에서 돌려보고 안 되는 부분이 있으면 알려주면 된다.
