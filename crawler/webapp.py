"""로컬 웹 UI: 지역 체크박스 + 개수 입력 후 버튼 클릭으로 크롤링을 실행한다.

사용법:
    pip install -r requirements.txt
    playwright install chromium
    python webapp.py
그다음 브라우저에서 http://127.0.0.1:5000 접속.
"""

import threading
import uuid
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_file
from playwright.sync_api import sync_playwright

from naver_esthetic_crawler import crawl_region, save_excel

app = Flask(__name__)

MAJOR_REGIONS = ["명동", "성수", "홍대", "강남", "압구정", "신사", "용산"]
RESULTS_DIR = Path(__file__).parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# job_id -> {"status": "running"|"done"|"error", "logs": [...], "file": str|None}
JOBS = {}


def run_job(job_id, regions, keyword, max_count, headless):
    job = JOBS[job_id]

    def log(msg):
        job["logs"].append(msg)

    all_places = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=headless)
            page = browser.new_page()
            for region in regions:
                try:
                    places = crawl_region(page, region, keyword, max_count, log=log)
                    all_places.extend(places)
                except Exception as e:
                    log(f"[ERROR] '{region}' 처리 중 오류: {e}")
            browser.close()

        output_path = RESULTS_DIR / f"{job_id}.xlsx"
        save_excel(all_places, output_path, log=log)
        job["file"] = str(output_path)
        job["status"] = "done"
    except Exception as e:
        log(f"[FATAL] {e}")
        job["status"] = "error"


@app.route("/")
def index():
    return render_template("index.html", major_regions=MAJOR_REGIONS)


@app.route("/crawl", methods=["POST"])
def start_crawl():
    data = request.get_json(force=True)
    checked = data.get("regions") or []
    custom_raw = data.get("custom_regions") or ""
    custom = [r.strip() for r in custom_raw.split(",") if r.strip()]
    regions = list(dict.fromkeys(checked + custom))  # 순서 유지 중복 제거

    if not regions:
        return jsonify({"error": "지역을 최소 1개 선택하거나 입력해줘"}), 400

    try:
        max_count = int(data.get("max_count") or 15)
    except ValueError:
        return jsonify({"error": "개수는 숫자로 입력해줘"}), 400
    max_count = max(1, min(max_count, 100))

    keyword = (data.get("keyword") or "에스테틱").strip()
    headless = bool(data.get("headless"))

    job_id = uuid.uuid4().hex[:8]
    JOBS[job_id] = {"status": "running", "logs": [], "file": None}
    threading.Thread(
        target=run_job, args=(job_id, regions, keyword, max_count, headless), daemon=True
    ).start()
    return jsonify({"job_id": job_id})


@app.route("/status/<job_id>")
def status(job_id):
    job = JOBS.get(job_id)
    if not job:
        return jsonify({"error": "존재하지 않는 작업"}), 404
    return jsonify({"status": job["status"], "logs": job["logs"]})


@app.route("/download/<job_id>")
def download(job_id):
    job = JOBS.get(job_id)
    if not job or not job.get("file"):
        return "아직 파일이 준비되지 않았어", 404
    return send_file(job["file"], as_attachment=True, download_name="seoul_esthetic_list.xlsx")


if __name__ == "__main__":
    app.run(debug=False, port=5000)
