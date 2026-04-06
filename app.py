import json
import os
from flask import Flask, render_template, jsonify, send_file, abort

app = Flask(__name__)

PROJECTS_FILE = "projects.json"
CV_FILE = os.path.join("static", "cv", "MatveiVasetsov_CV.pdf")


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
    if not os.path.exists(CV_FILE):
        abort(404)
    return send_file(
        CV_FILE,
        as_attachment=True,
        download_name="MatveiVasetsov_CV.pdf",
        mimetype="application/pdf",
    )


if __name__ == "__main__":
    app.run(debug=True)
