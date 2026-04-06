import io
import json
import os
from datetime import datetime
from flask import Flask, render_template, jsonify, send_file, request
from cv_generator import build_cv_pdf

app = Flask(__name__)

PROJECTS_FILE = "projects.json"


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
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    suffix = "RU" if lang == "ru" else "EN"
    filename = f"MatveiVasetsov_CV_{suffix}_{ts}.pdf"
    pdf_bytes = build_cv_pdf(lang)
    return send_file(
        io.BytesIO(pdf_bytes),
        as_attachment=True,
        download_name=filename,
        mimetype="application/pdf",
    )


if __name__ == "__main__":
    app.run(debug=True)
