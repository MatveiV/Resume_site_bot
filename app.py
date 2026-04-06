import json
import os
from flask import Flask, render_template, jsonify, send_file, abort, request

app = Flask(__name__)

PROJECTS_FILE = "projects.json"
CV_FILES = {
    "ru": os.path.join("static", "cv", "MatveiVasetsov_CV_RU.pdf"),
    "en": os.path.join("static", "cv", "MatveiVasetsov_CV_EN.pdf"),
}
# fallback: если нет языковой версии — отдаём любой существующий файл
CV_FALLBACK = os.path.join("static", "cv", "MatveiVasetsov_CV.pdf")


def load_projects():
    with open(PROJECTS_FILE, encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/projects")
def api_projects():
    return jsonify(load_projects())


@app.route("/download-cv")
def download_cv():
    lang = request.args.get("lang", "ru")
    cv_path = CV_FILES.get(lang, CV_FILES["ru"])
    if not os.path.exists(cv_path):
        cv_path = CV_FALLBACK
    if not os.path.exists(cv_path):
        abort(404)
    filename = f"MatveiVasetsov_CV_{'RU' if lang == 'ru' else 'EN'}.pdf"
    return send_file(cv_path, as_attachment=True, download_name=filename, mimetype="application/pdf")


if __name__ == "__main__":
    app.run(debug=True)
