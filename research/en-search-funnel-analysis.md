# SELLE 영어권 검색시장 구조 분석: 한국 피부과·미용시술 Google 검색 퍼널

**대상 시장**: 영어권 (미국·싱가포르·호주·캐나다·영국) | **작성일**: 2026-08-17 | **범위**: Google Ads 키워드 전략 수립을 위한 검색 수요 구조 분석

---

## 0. 조사 방법 및 데이터 한계 (먼저 읽어야 함)

### 0.1 검증한 가설

- **가설 A**: 아직 발견 못한 월 수만~수십만 규모의 Mega Keyword가 존재하고, 거기서 의료미용 고객이 파생된다.
- **가설 B**: Mega Keyword는 없고, 수요가 수백~수천 개 Long-tail로 분산되어 있다.
- 부가 가설: 검색량과 실제 환자 수의 괴리는 (i) 검색 채널 자체가 Google이 아니거나 (ii) 환자 다수가 영어권이 아니기 때문일 수 있다.

### 0.2 조사 순서 (실제 수행)

1. 한국 정부 외국인환자 통계 (KHIDI/보건복지부) — 실제 시장 크기와 국적·진료과 구성 확보
2. 키워드 자동완성·Google Trends·검색량 데이터 수집
3. 후보 키워드 SERP(검색결과) 구성 분석 → Medical Intent % 산출
4. Reddit/TikTok/YouTube/여행 커뮤니티에서 실제 사용자 언어 채굴
5. 경쟁 플랫폼 리버스엔지니어링 + K-pop/셀럽 발견 퍼널 검증

각 항목은 병렬 조사 후 교차 검증했다.

### 0.3 이번 조사 환경의 한계 (반드시 인지할 것)

이 세션의 네트워크 환경에서 다음 사이트/도구에 대한 **직접 접근이 차단**되었다: Ahrefs, Semrush, kwrds.ai, Ubersuggest, Google Trends 대시보드, Reddit, Quora, TripAdvisor, mohw.go.kr/khidi.or.kr 원문 PDF. 따라서:

- **검색량(Search Volume) 절대수치는 대부분 확보하지 못했거나 저신뢰(2차 인용)다.** 아래 모든 표에서 이런 경우 명시적으로 `N/A` 또는 "저신뢰"로 표기했다.
- **SERP 의도 분류, 정부 통계(언론 경유), 커뮤니티 언어 패턴, 경쟁사 콘텐츠 전략은 비교적 견고한 근거**를 확보했다 — 이 보고서의 핵심 결론은 대부분 이 세 가지에 기반한다.
- **권장**: 사용자가 보유한 KeywordTool.io / Google Keyword Planner 접근권으로 아래 "Bridge Keyword"·"Bottom Funnel" 후보 키워드 리스트의 실제 볼륨을 직접 재확인하는 것이 이 보고서보다 정확하다. 이 보고서의 가치는 **"어떤 키워드를 찾아봐야 하는지"와 "왜 그런 구조인지"**에 있다.

---

## 1. 핵심 발견 요약

1. **가설 B가 실제 데이터와 일치한다.** Mega Keyword는 존재하지 않는다. 다만 이유가 예상과 다르다 — 큰 볼륨의 상위 키워드("korean skincare", "k beauty", "glass skin")는 실제로 존재하지만, 이들의 **Medical/Clinic Intent는 SERP 분석 결과 0~13%**로 사실상 화장품/홈케어 시장이다. 즉 "우리가 못 찾은 Mega Keyword"가 아니라 "Mega Keyword는 있지만 SELLE의 고객이 아니다"가 맞는 설명이다.

2. **가장 중요한 단일 발견: 단어 하나가 검색 의도를 뒤집는다.** SERP 분석에서 `glass skin` (Medical Intent ~11%) → `glass skin treatment` (Medical Intent **~100%**)로, "treatment" 한 단어 추가만으로 의도가 완전히 역전됐다. 반면 `korean skin treatments`(17%), `korean skincare treatments`(13%)는 "treatment"가 들어가 있어도 낮다 — 즉 규칙은 "treatment를 붙이면 무조건 의료의도가 된다"가 아니라, **"skincare/skin"은 이미 화장품 SEO가 검색결과를 장악한 상태라 뒤에 뭘 붙여도 잘 안 뒤집히고, "glass skin"·"aesthetic"처럼 상대적으로 덜 포화된 조합에 구체적 수식어가 붙을 때 의도가 뒤집힌다**는 것이다. 이것이 이번 조사가 찾아낸 실질적 Bridge Keyword 메커니즘이다.

3. **환자수-검색량 괴리의 가장 큰 원인은 "채널 이탈"이 아니라 "언어 구성"이다.** 2025년 한국 외국인 피부과+성형 환자는 약 149만 명으로 추정되지만, 국적별로 보면 일본(29.9%)+중국(30.8%)이 60% 이상을 차지한다. 영어권(미국+캐나다+싱가포르, 확인 가능한 국가 합산)은 전체의 약 12%(24만 명)이며, 여기서 다시 피부과/성형 비중을 적용하면 **연간 13만~15만 명 수준**으로 추정된다. 애초에 "영어 검색으로 보이는 시장"이 처음부터 그렇게 크지 않을 가능성이 높다.

4. **Google 검색을 우회하는 구체적 채널이 확인됐다.** (a) 강남언니의 글로벌 앱 "UNNI"(2023년 출시, 도메인 내 1,800+ 클리닉·130만+ 리뷰) — 앱 내 검색/예약이 이루어져 Google 키워드 자체가 발생하지 않음. (b) 한국 체류 중에는 외국인도 Naver를 더 많이 쓴다는 증언 다수. (c) TikTok/YouTube의 "I tried a Korean skin clinic" 브이로그가 실질적 발견·검증 채널로 기능. (d) K-pop/셀럽 콘텐츠(제니×Reberry 클리닉 사례 등)가 존재하지만 대부분 화장품/루틴 소비로 끝나고 클리닉명까지 도달하는 콘텐츠는 소수.

5. **일부 시술/클리닉은 이미 브랜드명으로 인지되고 있다.** 일반 외국인 사용자들이 자연어로 "Rejuran", "물광주사/Water Glow Injection"을 직접 언급하는 사례가 다수 확인됐다 — 이는 브랜드 키워드 캠페인(예: "rejuran korea", "water glow injection seoul")의 근거가 된다.

---

## 2. 재설계된 Search Funnel (가설 대비 실제 데이터)

원래 가설(8단계: Aspiration → Outcome → Category → Problem → Treatment → Provider → Commercial → Transaction)은 구조적으로는 맞지만, **각 단계 사이의 연결이 Google 검색으로는 거의 보이지 않는다**는 것이 핵심 수정사항이다.

```
[Level 1] K-pop/셀럽 콘텐츠 ─┐
                             ├─→ 대부분 TikTok/YouTube/Instagram 안에서 소비, Google 이탈 거의 없음
[Level 2] Glass Skin / K-뷰티 욕구 ─┘        (SERP 확인: "korean glass skin" 의료의도 11%)

        ↓ (여기서 Google 검색으로 "새는" 비율은 낮음 — 대부분 제품/루틴으로 충족됨)

[Level 3] Bridge Zone (이번 조사의 핵심 발견)
   glass skin TREATMENT / korean AESTHETIC treatments / 지명(seoul/korea)+제공자(clinic/dermatologist)
   → 여기서 처음으로 SERP Medical Intent가 40~100%로 점프

        ↓

[Level 4~6] Treatment(rejuran, botox, ultherapy...) + Provider(clinic/dermatologist) + Seoul/Korea
   → 이 단계에서 "foreigner-friendly / for foreigners / english speaking" 라는 명시적 필터 키워드가 강하게 등장
   → 동시에 경쟁 "for foreigners" SEO 사이트들이 이 단계를 이미 장악 중

        ↓

[Level 7] Price/Cost/Worth it/Review/Reddit
   → "is it worth it", "is it cheaper in korea", "beauty bargain or scam" 같은 신뢰/비교 질문형이 강하게 관찰됨
   → 순수 가격 검색보다 "신뢰 검증형" 질문이 실제로는 더 흔함

        ↓

[Level 8] 예약
   → Google 검색이 아니라 클리닉 사이트 직접 문의, 에이전시, 또는 강남언니류 앱에서 발생하는 경우가 다수로 추정
```

**결론: Funnel 자체는 실재하지만, Google에서 관찰 가능한 것은 Level 3(Bridge) 이후뿐이다.** Level 1~2는 실질적으로 다른 플랫폼(TikTok/YouTube)의 내부 검색 데이터이며 Google Keyword Planner에 잡히지 않는다.

---

## 3. 결과 테이블 1 — Mother Keyword (검색량 순)

| Keyword | Monthly Volume | Source | Primary Intent | Medical Intent % | Relevance to SELLE | Notes |
|---|---:|---|---|---:|---|---|
| skincare (broad) | ~2,700,000 (저신뢰) | kwrds.ai 2차 인용 | Products | 0% | 없음 | 검증 불가, 참고용 |
| skincare routine | ~1,000,000 (저신뢰) | kwrds.ai 2차 인용 | Routine | 0% (추정) | 없음 | 검증 불가 |
| korean skincare | ~550,000 (저신뢰) | kwrds.ai 2차 인용 | Products/Routine | 0% (SERP 실측) | 낮음 | SERP 실측: Sulwhasoo/YesStyle/Soko Glam/Sephora 등 전부 제품 판매 |
| k beauty | N/A | — | Products/Culture | 0% (SERP 실측) | 낮음 | SERP 실측: Coveteur/Wikipedia/YesStyle 등, 클리닉 0건 |
| korean beauty | N/A | — | Culture/Products | N/A | 낮음 | 미확인 |
| glass skin | N/A | — | Desired Outcome | ~11% (SERP 실측, "korean glass skin" 기준) | 낮음~중간 | Bridge 직전 단계, 단독으로는 화장품/루틴 |
| korean skincare routine | N/A | — | Routine | N/A | 낮음 | 미확인 |
| medical tourism korea | 원 제보 기준 "월 수백~수천" | 사용자 KeywordTool.io | Tourism/Medical | **78%** (SERP 실측) | **높음** | 볼륨은 작지만 의도 순도가 매우 높음 — Mother보다는 Bridge에 가까움 |
| korean aesthetic treatments | N/A | — | Category | **71%** (SERP 실측) | **높음** | 볼륨 미확인이나 의도 순도 최상위권 |
| korean facial | N/A | — | Facial/Spa | 20% (SERP 실측) | 중간 | 미국 로컬 스파 결과가 다수 섞임(비한국) |

> **관찰**: "진짜 큰 검색량"과 "의료 의도"는 이 리스트에서 거의 반비례한다. 확인 가능한 볼륨이 클수록 Medical Intent가 0%에 수렴하고, Medical Intent가 높을수록(medical tourism korea, korean aesthetic treatments) 원 제보자가 이미 관찰한 대로 볼륨이 작다. 이것이 가설 A(숨은 Mega Keyword)를 기각하는 가장 직접적인 증거다.

---

## 4. 결과 테이블 2 — Bridge Keyword

**정의**: 일반적 K-Beauty 관심에서 실제 한국 오프라인 시술 소비로 검색 의도가 전환되는 지점. Medical Intent %는 SERP 실측(상위 결과 유형 분류) 기준.

| Keyword | Monthly Volume | Medical Intent % | Commercial Intent | Funnel 단계 | Why Important |
|---|---:|---:|---|---|---|
| glass skin treatment | N/A | **~100%** | 높음 | Bridge 진입점 | "treatment" 추가만으로 11%→100% 역전된 핵심 사례. NewBeauty, Dr David Jack 클리닉, mineclinic.com("for tourists") 등이 실제 상위 노출 |
| korean glass skin treatment | N/A | **57%** | 높음 | Bridge | 관광객 타깃 클리닉(mineclinic.com) 및 미용의료 사이트가 절반 이상 |
| aesthetic clinic seoul | N/A | **~100%** | 매우 높음 | Bridge→Provider | Creatrip(관광 예약 플랫폼) 포함 전 결과가 클리닉 |
| dermatologist seoul | N/A | **~100%** | 매우 높음 | Bridge→Provider | "for Foreigners"를 명시한 사이트(koreaskinclinic.net, medicalaesthetickorea.com) 다수 |
| best skin clinic seoul | N/A | **~100%** | 매우 높음 | Bridge→Commercial | "Top 15... for Foreigners" 류 콘텐츠가 이 키워드를 정확히 타깃팅 중 |
| skin clinic seoul | N/A | **80%** | 높음 | Bridge→Provider | 실제 한국 클리닉 자사 사이트가 직접 노출(대부분 영어 페이지 보유) |
| medical tourism korea | 원 제보 기준 저볼륨 | **78%** | 높음 | Bridge(상위) | Bookimed, Seoul Guide Medical 등 브로커 플랫폼 다수 노출 |
| korean aesthetic treatments | N/A | **71%** | 중간~높음 | Bridge(상위) | PubMed 학술 결과와 클리닉 결과가 혼재 — 카테고리 자체의 인지도는 아직 형성 중 |
| rejuran korea | N/A | 43% | 매우 높음(바텀퍼널) | Treatment(브랜드) | 실사용자 언어 채굴에서 가장 많이 "이름으로" 언급된 시술 |
| botox korea | N/A | 38% | 높음 | Treatment | 가격비교 브로커(Bookimed) 노출, 일부 도매/그레이마켓 결과 혼입 |
| water glow injection / 물광주사 | N/A | 미실측(질적 근거만) | 높음 | Treatment(브랜드) | TikTok에서 실사용자가 한국어 원어까지 병기하며 언급 — 영어 캠페인에서 "water glow injection"이 rejuran 다음으로 인지도 높은 시술명 |
| english speaking clinic seoul / gangnam | N/A | 질적으로 높음(직접 SERP 미실측) | 매우 높음 | Provider Filter | 커뮤니티 조사에서 "영어가 되는가"가 반복 등장하는 실질적 필터 조건 |
| korean skin clinic for foreigners | N/A | 질적으로 높음 | 높음 | Provider Filter | 경쟁사들이 이미 이 정확한 문구 패턴으로 콘텐츠 제목을 짓고 있음(리버스엔지니어링 확인) |
| is [treatment] worth it in korea | N/A | 질적으로 높음 | 높음(전환 직전) | Commercial(신뢰검증) | "beauty bargain or the next Turkey?"(Euronews) 같은 신뢰형 질문이 실제 존재 |
| is botox cheaper in korea | N/A | 질적 근거(cheongdamskinclinic.com 등 실제 타깃 콘텐츠 존재) | 높음 | Commercial | 자국 대비 가격 비교 프레임 — 매우 구체적인 구매 직전 신호 |
| korean beauty clinic where idols go | N/A | 질적 근거만(콘텐츠 카테고리로 확인) | 중간 | Aspiration→Bridge | K-pop 발견 퍼널의 실제 접점, 단 전환까지는 미확인 |
| glow up korea trip / korea skin treatment itinerary | N/A | 질적 근거(경쟁사 블로그 제목 패턴) | 높음 | Bridge→Package | "One-Week Korean Skin Treatment Itinerary" 등 여행+시술 결합 콘텐츠 존재 |
| gangnam unni / unni app | N/A | N/A(브랜드 검색) | 매우 높음이나 SELLE 경쟁자로 유입 | Provider(경쟁) | 직접 키워드 타깃은 아니지만, 이 앱이 흡수하는 검색을 SELLE가 가로채야 할 대상 |
| cinderella injection / snow white injection korea | N/A | 질적 근거만 | 중간~높음 | Treatment(브랜드, 별칭) | 글루타치온 시술을 성분명이 아닌 별명으로 검색하는 패턴 확인 |
| juvelook korea | N/A | 질적 근거만(경쟁 브랜드 언급) | 높음 | Treatment(브랜드) | Rejuran과 나란히 언급되는 2위권 스킨부스터 브랜드 |

**Effective Medical Search Volume**: 대부분 항목에서 Monthly Volume 자체가 `N/A`이므로 `Volume × Medical Intent%` 계산은 신뢰성 있게 산출할 수 없다. **이 표에서 실제로 산출 가능했던 것은 Medical Intent %뿐이며, 이것이 이번 조사의 핵심 산출물이다.** 사용자가 Keyword Planner로 위 20개 키워드의 실측 볼륨만 채워 넣으면 이 표는 바로 완성된다.

---

## 5. 결과 테이블 3 — Bottom Funnel Keyword Cluster

개별 롱테일이 아니라 **의미 단위 클러스터** 기준. Combined Volume은 대부분 확보하지 못해 정성 등급(Low/Medium/High, 상대비교)으로 표기.

| Keyword Cluster | Combined Volume (정성) | Intent | Conversion Potential | Competition | Recommended Landing |
|---|---|---|---|---|---|
| Rejuran/스킨부스터 + Korea/Seoul (+price) | Medium | 매우 명확한 시술 브랜드 탐색 | 높음 | 낮음~중간 (전문 SEO사이트 소수) | 시술 상세 + 가격표 + 예약 CTA |
| Botox/보톡스 + Korea/Seoul (+price) | Medium | 가격 비교형 | 높음 | 중간 (브로커 사이트 존재) | 가격 비교표 + 한국 vs 자국 비교 |
| Ultherapy/Thermage(리프팅) + Korea | Low~Medium | 구체적 시술 탐색 | 높음 | 낮음 | 시술 설명 + 리프팅 전후사진 |
| 클리닉 브랜드명(Reberry, VS Line, Cheongdam Esmin, Upic, FINE, WOOA, MI&MI 등) + price/review | Low(개별)/Medium(합산) | 브랜드 신뢰 검증 | 매우 높음(이미 결정 근접) | 낮음(각 클리닉명은 경쟁 적음) | 클리닉별 랜딩 + 리뷰 집계 |
| "best/top skin clinic seoul for foreigners" | Medium | 비교/큐레이션 탐색 | 높음 | **높음** (경쟁 콘텐츠 사이트 다수 이미 장악) | SELLE 자체 큐레이션 랭킹 페이지 |
| "dermatologist seoul english speaking" | Low~Medium | 필터형(언어장벽 해소) | 매우 높음 | 중간 | 영어가능 의료진 프로필 랜딩 |
| "is [treatment] worth it in korea" / "is it cheaper in korea" | Low(개별)/Medium(합산) | 신뢰검증형 | 중간~높음 | 낮음(질문형 콘텐츠 공급 부족) | 비교/신뢰 콘텐츠(가격+부작용+후기) |
| 여드름/색소침착 치료(acne/pigmentation treatment korea) | Low | Problem-driven | 중간 | 낮음 | 문제별 솔루션 랜딩 |
| 안면윤곽/브이라인(v-line, jaw, face slimming) + korea | Low~Medium | 아웃컴 지향 | 중간 | 낮음~중간 | 아웃컴 기반 랜딩(전후사진 중심) |
| 성형 카테고리(rhinoplasty/double eyelid korea) | Medium | 참고 카테고리(SELLE 핵심 아님) | 낮음(피부과 중심 전략과 어긋남) | 높음(대형 성형 플랫폼 존재) | SELLE 1차 전략에서 제외 권장 |
| Cinderella/Snow White/글루타치온 injection korea | Low | 브랜드/별칭형 | 중간 | 낮음 | 별칭 그대로 사용한 랜딩(SEO 기회) |
| 물광주사/water glow injection seoul | Low | 브랜드형(원어 병기) | 높음 | 낮음(경쟁 거의 없음) | 한국어 원어 병기 랜딩 — 니치 기회 |
| "korea skin treatment itinerary / package" | Low | 여행+시술 결합 | 높음(번들 구매) | 낮음 | 여행일정+시술 패키지 상품 페이지 |
| medical tourism agency/broker 대체 키워드("book skin clinic seoul") | Low | 예약 직전 | 매우 높음 | 중간(Bookimed 등 브로커 존재) | 즉시 예약 플로우 |

> **가장 중요한 관찰**: 개별 클러스터는 대부분 "Low"지만, **14개 클러스터를 합산하면 원 제보자가 우려했던 "수십~수백 검색"보다 실질적으로 큰 시장**이 된다. 이것이 가설 B(분산된 롱테일 합산)를 지지하는 구조적 근거다.

---

## 6. 결과 테이블 4 — Search Journey (정성)

실측 전환율 데이터는 확보하지 못해 정성 등급(High/Medium/Low)으로 표기. 확보한 SERP·언어 증거를 근거로 각 화살표의 "실재 가능성"을 평가했다.

```
K-pop / Korean Celebrity 콘텐츠
   ↓ Low  (대부분 TikTok/YouTube 내부에서 소비 종료, Google로 새는 비율 낮음)
Glass Skin / Korean Beauty 관심
   ↓ Low  (SERP 실측: "korean glass skin" 의료의도 11% — 대부분 제품/루틴으로 충족되어 이탈)
Glass Skin Treatment / Korean Aesthetic Treatments   ← ★Bridge 진입
   ↓ Medium~High (SERP 실측: 여기서부터 의료의도 57~100%로 급상승 — 실제 전환이 일어나는 구간)
Skin Clinic Seoul / Dermatologist Seoul / Aesthetic Clinic Seoul
   ↓ High (SERP 실측: 80~100% 의료의도, "for foreigners" 콘텐츠가 이 단계를 정조준)
Rejuran Korea / Botox Korea / Water Glow Injection (구체적 시술 브랜드)
   ↓ High (커뮤니티 언어 채굴: 실사용자가 브랜드명을 직접 호명 — 구매 직전 신호)
Price / Worth it / English Speaking / Review (신뢰·조건 검증)
   ↓ Medium (Google 검색으로 마무리되기도 하지만, 이 지점부터 예약은 앱/DM/에이전시로 이탈하는 사례가 다수 확인됨)
Booking (예약)
```

**핵심 시사점**: Google 검색으로 관찰 가능한 전환은 "Bridge → Provider → Treatment" 구간에 집중되어 있다. 위쪽(K-pop→Glass Skin)과 아래쪽(신뢰검증→예약) 양 끝단은 Google 밖(TikTok/YouTube, 앱/DM/에이전시)에서 일어날 가능성이 높다.

---

## 7. Hidden Keyword 발굴 결과 (요청하지 않았던 것들)

### 7.1 실사용자 언어 (Reddit/TikTok/YouTube/TripAdvisor)
- 자연어 질문형: *"skin care clinic recommendation"*, *"is [treatment] worth it in Korea"*, *"is Botox cheaper in Korea"*, *"do I need to speak Korean at these clinics"*, *"beauty bargain or the next Turkey?"*
- "관광객 전용이 아니라 현지인도 가는 곳"을 원하는 역설적 니즈: *"primarily serves Korean patients"*를 오히려 신뢰 신호로 찾는 패턴 확인 — "for foreigners"만 내세우면 오히려 바가지 우려를 유발할 수 있음
- YouTube 제목 패턴: *"I Tried a Korean GLASS SKIN FACIAL in Seoul"*, *"I Got a $650 Korean Glass Skin Facial"*, *"is this legit??"* — "I tried/got + 가격 + legit?" 포맷이 매우 반복적
- 브랜드로 인지되는 시술 순위: **Rejuran > 물광주사(Water Glow Injection) > Botox/K-Botox > Ultherapy/Thermage > Cinderella/Snow White Injection > Juvelook > V-line injection > Inmode**
- 실사용자가 언급하는 클리닉명: VS Line Clinic, Reberry, Cheongdam Esmin, Upic, FINE, WOOA, MI&MI, ID Hospital, Xenia, MediCube

### 7.2 경쟁사 리버스엔지니어링
- **가장 강력한 직접 경쟁자**: 강남언니의 글로벌 앱 "UNNI"(2023 출시, 13개 언어, 도메인 내 1,800+ 클리닉·130만+ 리뷰, 이미 일본에서 70만+ 유저 확보) — SELLE는 이 앱이 흡수하는 검색/예약 수요를 명확히 인지하고 차별화 포인트를 잡아야 함
- 소규모 "for foreigners" SEO 사이트 다수가 이미 정확히 이 보고서의 Bridge/Bottom Funnel 구간을 타깃팅 중: 반복되는 제목 패턴 = *"Top N Skin Clinics in Seoul for Foreigners (Year Guide)"*, *"[Treatment] Cost Seoul: Price Guide + Best Clinics"*, *"One-Week Korean Skin Treatment Itinerary"*
- 패키지 네이밍 관행: "Signature/Timeless/Ultimate Package" 식 티어링이 업계 표준처럼 반복됨

### 7.3 K-pop/셀럽 발견 퍼널 검증
- 실재하는 연결고리: 제니(BLACKPINK) × Reberry Clinic(명동) 언론 노출, "아이돌이 다니는 클리닉" 카테고리 콘텐츠(Circle Clinic, YD Clinic 등 실명 언급)
- 그러나 대부분의 Glass Skin/K-pop 스킨케어 콘텐츠는 "전문 시술이 있다"는 사실은 인정하면서도 **클리닉명·가격까지 연결하지 않고 끝남** — 이 단절 지점이 SELLE에게는 콘텐츠 기회(제니가 받은 시술이 정확히 무엇이고 어디서 예약 가능한지 연결하는 콘텐츠는 아직 공급 부족)

---

## 8. 최종 질문 10개에 대한 답변

**1. 영어권 외국인이 사용하는 가장 큰 검색어 30개는?**
검색량 기준 상위권은 대부분 순수 화장품/문화 키워드(korean skincare, k beauty, skincare routine, glass skin, korean beauty)이며, 이들은 SELLE 잠재고객과 직접 연결되지 않는다. Medical Intent가 확인된 키워드들(섹션 4·5의 20+14개)이 실질적으로 SELLE와 관련된 "빅 리스트"이며, 볼륨 자체는 개별로는 작다. 30개를 강제로 채우기보다, **"볼륨은 크지만 무관한 키워드"와 "볼륨은 작지만 관련된 키워드"를 섞지 않는 것**이 이번 조사의 결론이다.

**2. 실질적으로 의료미용으로 연결되는 검색어는?**
섹션 4(Bridge, 20개)와 섹션 5(Bottom Funnel, 14개 클러스터)가 그 답이다. 공통 패턴: **"glass skin/aesthetic" + treatment**, **지명(seoul/korea) + 제공자(clinic/dermatologist)**, **구체 시술 브랜드명(rejuran, water glow injection)**.

**3. 월 10,000+ 검색량이면서 SELLE와 연결 가능한 키워드는 존재하는가?**
**이번 조사로는 확인하지 못했다.** 확인된 고순도 의료의도 키워드(aesthetic clinic seoul, dermatologist seoul, best skin clinic seoul 등)는 원 제보자의 KeywordTool.io 관찰과 일치하게 저볼륨으로 추정된다. "10K+이면서 SELLE향"인 키워드가 존재한다면, 이번 조사가 놓친 영역이라기보다 **애초에 그런 키워드가 구조적으로 존재하기 어렵다**(볼륨과 의도가 반비례)는 것이 이번 조사의 잠정 결론이다. 사용자가 실측 도구로 직접 재확인할 것을 권장한다.

**4. 월 100,000+ 규모 Mother Keyword에서 의료미용으로 연결되는 Funnel이 존재하는가?**
korean skincare(추정 55만) 같은 키워드는 규모는 충족하지만 **SERP 실측상 Funnel이 Google 안에서 이어지지 않는다**(0% 의료의도, 상위 결과 전부 커머스). Funnel 자체는 행동적으로 존재할 수 있으나, Google 검색이라는 단일 채널 안에서 추적 가능한 형태로는 존재하지 않는다.

**5. 가장 중요한 Mother Keyword 10개는?**
섹션 3 표 참조. 다만 "Mother Keyword"라는 카테고리 자체가 SELLE에게는 낮은 우선순위임을 명확히 해야 한다 — 이들은 광고 타깃보다는 **콘텐츠/SEO 상위 퍼널(브랜드 인지) 용도**로만 가치가 있다.

**6. 가장 중요한 Bridge Keyword 20개는?**
섹션 4 표. 최우선 5개: `glass skin treatment`, `aesthetic clinic seoul`, `dermatologist seoul`, `best skin clinic seoul`, `medical tourism korea`.

**7. 가장 중요한 Bottom Funnel Keyword Cluster 20개는?**
섹션 5 표(14개 클러스터로 압축, 각각 세부 롱테일 다수 포함). 최우선 3개: Rejuran/스킨부스터 클러스터, 클리닉 브랜드명 클러스터, "best skin clinic seoul for foreigners" 클러스터.

**8. Mega Keyword 전략 vs Long-tail 집합 전략, 어느 쪽이 적합한가?**
**Long-tail 집합 전략이 명확히 우세하다.** Mega Keyword 후보는 전부 의료의도가 0~13%로 낮아 Google Ads 타깃으로 부적합하다. 반면 Bridge+Bottom Funnel을 합산하면 (a) 의도 순도가 높고 (b) 경쟁이 상대적으로 낮으며 (c) 클러스터 합산 시 무시할 수 없는 규모가 된다.

**9. Google Search는 실제로 얼마나 중요한 채널인가?**
**"발견(Discovery)" 채널로서는 제한적, "검증·비교(Validation)" 채널로서는 중요**하다는 것이 근거 기반 결론이다. 발견은 TikTok/YouTube/K-pop 콘텐츠, 그리고 강남언니 같은 앱이 상당 부분 담당하는 것으로 보이며, Google은 사용자가 이미 특정 시술/지역을 어느 정도 인지한 뒤 "가격이 얼마인지, 진짜 괜찮은지, 영어가 되는지"를 확인하는 단계(Bridge~Commercial)에서 결정적 역할을 한다.

**10. 검색량과 실제 외국인 환자 숫자의 괴리는 어떻게 설명되는가?**
가장 크게 기여하는 3가지, 근거 강도 순:
- **(근거 강함) 언어 구성**: 2025년 환자의 60%+ 가 중국어/일본어권. 영어권은 처음부터 전체의 ~12%(약 24만 명, 피부과+성형으로 좁히면 13~15만 명 추정)에 불과 — "괴리"의 상당 부분은 애초에 시장 자체가 작기 때문.
- **(근거 있음) 채널 분산**: 강남언니/UNNI 앱, Naver 검색, TikTok/YouTube 내부 검색이 Google 영어 키워드 도구에 잡히지 않는 수요를 상당량 흡수.
- **(근거 있음이나 정량화 안 됨) 에이전시/브로커 중개**: Bookimed 등 브로커가 여러 클리닉을 대신 검색해주는 구조 — 1명의 환자가 여러 Google 검색을 발생시키지 않고 브로커 1회 접촉으로 끝나는 경우 다수.

---

## 9. 최종 전략 제안

이번 조사 데이터가 가리키는 구조는 명확히 **"Long-tail 집합 + Intent 우선순위" 모델**이며, 단일 Mega Keyword 베팅은 데이터로 뒷받침되지 않는다.

### 9.1 Google Ads 캠페인 구조 (우선순위 순)

1. **1순위 — Bridge/Provider 키워드 캠페인** (섹션 4): `aesthetic clinic seoul`, `dermatologist seoul`, `best skin clinic seoul`, `skin clinic seoul`, `medical tourism korea`, `glass skin treatment`. 볼륨은 작지만 의도 순도가 최상급이며, 경쟁이 상대적으로 낮다. 광고 예산의 핵심을 여기 배치.
2. **2순위 — 시술 브랜드 + 클리닉 브랜드 키워드** (섹션 5): rejuran/botox/water glow injection + korea/seoul, 그리고 실사용자가 이미 이름을 아는 클리닉 브랜드(Reberry, VS Line 등)의 자체 브랜드 방어/비교 키워드. 전환 직전 신호이므로 CPA 목표를 가장 공격적으로 설정 가능.
3. **3순위 — 신뢰검증형 질문 키워드**: "is [treatment] worth it in korea", "is botox cheaper in korea" 류. 경쟁 콘텐츠가 부족한 니치이며, 랜딩페이지를 비교/신뢰 콘텐츠로 구성하면 CTR·전환 모두 유리할 가능성.
4. **4순위(광고 X, SEO/콘텐츠로) — Mother Keyword**: korean skincare, k beauty, glass skin 등은 유료광고 타깃에서 제외하고, 브랜드 인지·SEO 콘텐츠(블로그, YouTube)로만 다룬다. 이 단계에 광고비를 태우는 것은 이번 데이터상 비효율적이다.

### 9.2 구조적 실행안

```
Bottom Funnel Keyword Cluster (14개, 수백 개 롱테일 포함)
        ↓
Intent별 Programmatic Landing Page 자동 생성
  - 시술별 랜딩 (rejuran / botox / water glow injection / ultherapy ...)
  - 클리닉 브랜드별 랜딩 (경쟁사가 이미 선점한 "for foreigners" 큐레이션 대체)
  - 신뢰검증형 콘텐츠 랜딩 ("is it worth it", "cheaper in Korea" 비교 페이지)
        ↓
Google Ads Long-tail Capture (섹션 4·5 키워드 전량)
        ↓
SEO Programmatic Landing Pages (Ads로 검증된 키워드 중 CPC 부담이 큰 것은 SEO로 전환)
        ↓
예약 (앱 내 예약 플로우 — 강남언니/UNNI와 정면 승부하려면 예약 마찰을 최소화해야 함)
```

### 9.3 데이터로 뒷받침되지 않는 것 (하지 말아야 할 것)

- **"korean skincare", "k beauty", "glass skin" 등에 대한 대규모 Search Ads 집행**: SERP 실측상 의료의도가 0~11%로, 클릭당 대부분 무관한 트래픽 유입 가능성이 높다.
- **"숨겨진 Mega Keyword를 더 찾아야 한다"는 전제하의 추가 키워드 리서치 확장**: 이번 조사에서 반증됐다. 대신 이미 확인된 Bridge/Bottom Funnel 클러스터의 **롱테일 변형(시술×도시×가격×리뷰 조합)을 최대한 늘리는 방향**이 데이터와 일치한다.
- **성형외과(rhinoplasty, 안검수술 등) 카테고리 확장**: 피부과 중심 SELLE 전략과 별개 시장이며, 이미 대형 플랫폼(강남언니 등)이 강하게 장악. 1차 전략에서 제외 권장.

---

## 10. 다음 액션 (사용자가 직접 확인해야 하는 것)

이 환경의 네트워크 제약으로 확보하지 못한 항목들 — 우선순위 순:

1. 섹션 4·5의 34개 키워드(Bridge 20 + Bottom Funnel 14 클러스터의 세부 롱테일)를 Google Keyword Planner/Ahrefs/Semrush로 실측 볼륨 확인 (미국/싱가포르/호주/캐나다/영국 분리)
2. KHIDI 원문 보고서(`2025년 외국인환자 유치실적 통계분석보고서`, khidi.or.kr, 2026년 중 발간 예정)에서 호주·영국 국적 데이터 및 진료과별 국적 교차표 확보 — 이번 조사에서는 두 국가 데이터를 찾지 못함(N/A)
3. Google Trends에서 "glass skin treatment", "aesthetic clinic seoul" 등 Bridge Keyword의 국가별(US/SG/AU/CA/UK) 관심도 직접 조회
4. 강남언니 UNNI 앱의 실제 트래픽/키워드 소스 조사(Similarweb 등, 이번 세션에서 접근 차단됨)

---

## 부록: 주요 출처

- 보건복지부(MOHW) 보도자료 "2024년 외국인 환자 유치 117만 명"(mohw.go.kr), "2025년 외국인 환자 유치 200만 돌파"(2026.04)
- Korea Biomedical Review, Korea Times(2026.04.24) — KHIDI 통계 인용 기사
- SCMP "Foreign dermatology patients in South Korea up 117-fold since 2009"
- Yahoo Finance / Etonne — 강남언니 UNNI 글로벌 앱 관련 보도
- Euronews "Are South Korea's cheap Botox clinics a beauty bargain or the next Turkey?" (2023.09)
- WebSearch 스니펫 기반 SERP 구성 확인 (17개 후보 키워드, 상위 6~10건씩 도메인/콘텐츠 유형 수동 분류)
- TikTok/YouTube/TripAdvisor 상 실사용자 게시물 제목·캡션(검색 스니펫 경유 확인, 원문 직접 접근은 차단됨)
- 사용자 제공 KeywordTool.io 관찰치(원본 데이터, 이번 조사가 직접 재현하지 못한 항목 다수 포함)

*모든 수치는 확인 가능한 출처가 있는 경우에만 기재했으며, 확인 불가 항목은 명시적으로 N/A 또는 저신뢰로 표기했다.*
