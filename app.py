import io
import json
import os
from datetime import datetime
from flask import Flask, render_template, jsonify, send_file, abort, request
from weasyprint import HTML

app = Flask(__name__)

PROJECTS_FILE = "projects.json"

CV_DATA = {
    "ru": {
        "name": "Матвей Евгеньевич Васецов",
        "subtitle": "Системный и бизнес-аналитик · Vibe-кодер · К.ф.-м.н.",
        "summary": (
            "Аналитик с 19-летним опытом в FinTech. Специализируюсь на трансляции бизнес-требований "
            "в архитектурные решения и MVP, проектировании высоконагруженных систем — торговых платформ "
            "и расчётных систем. Закрываю связку бизнес↔разработка: собираю требования, проектирую "
            "архитектуру и автоматизирую рутину на Python — вы экономите итерации и деньги."
        ),
        "labels": {
            "summary": "Профиль",
            "experience": "Опыт работы",
            "projects": "Проекты",
            "skills": "Технологии",
            "education": "Образование",
            "tech": "Стек",
        },
        "experience": [
            {
                "role": "Системный и бизнес-аналитик, Vibe-Developer",
                "company": "ИП (самозанятый)",
                "date": "07.2024 — н.в.",
                "desc": "Проектирование мультипровайдерной AI-архитектуры, FSM-конфигураторы, RAG-пайплайны, рефакторинг Python, REST API на Go, multi-stage Docker. Разработка и бэктестинг алгоритмических стратегий. Создание MVP-приложений: Telegram-боты, парсеры, генераторы PDF, сайт-резюме.",
                "achievements": [
                    "Единая OpenAI-совместимая архитектура для 5 провайдеров без изменения кода бота",
                    "AI-агент с 11 инструментами: два UI (CLI + Telegram) на едином ядре без дублирования кода",
                    "Порт Flask→Go: ×20 RPS при образе 10 МБ vs 150 МБ",
                    "Пайплайн транскрипция→PDF с 3 типами отчётов и base64-встраиванием изображений",
                ],
                "tech": "Python, Go, aiogram 3, FastAPI, Flask, LangChain, RAG, ChromaDB, Docker, GitHub Actions",
            },
            {
                "role": "Системный аналитик",
                "company": "Techcoredev.ru (АО «Инновационные технологии»)",
                "date": "04.2025 — 11.2025",
                "desc": "Система управления страховыми продуктами. Полный цикл спецификаций, BPMN/ERD/UML/C4, реверс-инжиниринг legacy с AI. Ускорил этап проектирования за счёт AI-генерации типовых фрагментов документации.",
                "achievements": [],
                "tech": "Node.js, DBeaver, MS SQL Server, Confluence, Cursor, Windsurf, PlantUML, Figma",
            },
            {
                "role": "Ведущий аналитик",
                "company": "Raccoonsoft.ru & Devexperts.com",
                "date": "04.2021 — 03.2024",
                "desc": "Tastyworks iPad (tastytrade.com) — акции, деривативы (опционы, фьючерсы), форекс, крипто. Выявление требований, user stories, UI/UX, реверс-инжиниринг мобильного/толстого/тонкого клиентов. Успешный вывод продукта на рынок.",
                "achievements": [],
                "tech": "JIRA, GitHub, Figma, Java, MindManager",
            },
            {
                "role": "Ведущий аналитик",
                "company": "ООО «ЛАНИТ-ТЕРКОМ»",
                "date": "12.2013 — 04.2025",
                "desc": "ЖКХ ВЦКП-ЕИРЦ, МЭШ ДИТ Москвы, Газпром нефть (ВЕГА ФЭМ, Цифровой двойник сейсморазведки), ЕМИАС (Раковый регистр), Toyota, AREA9, presale-оценки (Росатом, YOTA, Роснедра и др.).",
                "achievements": [],
                "tech": "Oracle, PostgreSQL, 1С, ARIS, Bizagi, Enterprise Architect, JIRA, Confluence, Kafka, Grafana",
            },
            {
                "role": "Бизнес/системный/финансовый аналитик",
                "company": "Devexperts.com",
                "date": "08.2007 — 05.2012",
                "desc": "ThinkOrSwim, GFT Dealbook 360, DXtrade — АТС, FX и бинарные опционы, технический анализ, дилинг, мобильные клиенты, FIX-интеграции, риск-менеджмент, бэк-офис.",
                "achievements": [],
                "tech": "DOORS, Polarion, JIRA, Enterprise Architect, FIX protocol",
            },
            {
                "role": "Старший аналитик бизнес-процессов",
                "company": "TKB BNP Paribas Investment Partners",
                "date": "05.2012 — 03.2013",
                "desc": "Model portfolio, Structured products, Value-at-Risk, CAPM, ATP, MTS-ATS-Robot, Data Quality, Data Mining. Спецификации для Front-Middle-Back Office и Risk Management.",
                "achievements": [],
                "tech": "QUIK, MetaTrader 4/5 (+MQL), 1C, MS SQL, yEd",
            },
            {
                "role": "Старший бизнес-аналитик",
                "company": "Deutsche Telekom IT Solutions",
                "date": "05.2013 — 12.2013",
                "desc": "De-mail — нотариальный E-mail. SRS + модели процессов (DFD, ERM, BPMN, UML) → успешное прохождение предварительного проектирования.",
                "achievements": [],
                "tech": "Polarion, JIRA, Confluence, Enterprise Architect",
            },
            {
                "role": "Бизнес-аналитик",
                "company": "Visual Trading Systems LLC",
                "date": "02.2006 — 08.2007",
                "desc": "АТС и Backtesting Engine для торговой платформы VT Trader (Capital Market Services FX).",
                "achievements": [],
                "tech": "VT Trader, MetaTrader (+MQL), MetaStock, Tradestation, Wealth-Lab",
            },
        ],
        "skills": [
            {"category": "Языки", "items": "Python 3.10+, Go 1.22, SQL, Java, Bash, MQL, TeX"},
            {"category": "AI / LLM", "items": "OpenAI API, Claude, Gemini, DeepSeek, GLM, Llama, Qwen; function calling, MCP, RAG, LangChain, ChromaDB"},
            {"category": "Фреймворки", "items": "FastAPI, Flask, aiogram 3, Pydantic, Jinja2, WeasyPrint, aiohttp"},
            {"category": "Данные", "items": "PostgreSQL, SQLite, Oracle, MS SQL Server, 1С, pandas, openpyxl, yfinance"},
            {"category": "ML", "items": "scikit-learn, LightGBM, PyTorch Lightning, LSTM, TFT, optuna, shap"},
            {"category": "Инфраструктура", "items": "Docker, Docker Compose, Grafana Loki, GitHub Actions"},
            {"category": "BA/SA", "items": "Confluence, JIRA, BPMN, UML, C4, PlantUML, Draw.io, Figma, ARIS, Bizagi, Enterprise Architect"},
            {"category": "Стандарты", "items": "PMBoK, BABOK, ГОСТ 34, IEEE 830, ISO/IEC/IEEE 29148"},
        ],
        "education": [
            {"degree": "К.ф.-м.н., Математическая кибернетика", "years": "1995–1998", "place": "СПбГУ, аспирантура, факультет прикладной математики и процессов управления"},
            {"degree": "Математик, Прикладная математика", "years": "1990–1995", "place": "СПбГУ, факультет прикладной математики и процессов управления"},
            {"degree": "Экономист, Финансы и кредит", "years": "1999–2002", "place": "СПбГУ (экономический факультет) и Международный банковский институт (МБИ)"},
        ],
    },
    "en": {
        "name": "Matvei Evgenyevich Vasetsov",
        "subtitle": "Systems & Business Analyst · Vibe-Coder · PhD in Mathematics",
        "summary": (
            "Analyst with 19 years of experience in FinTech. Specialising in translating business requirements "
            "into architectural decisions and MVPs, designing high-load systems — trading platforms and settlement engines. "
            "I bridge the business↔engineering gap: gather requirements, design architecture, and automate routine work "
            "in Python — saving you iterations and money."
        ),
        "labels": {
            "summary": "Profile",
            "experience": "Work Experience",
            "projects": "Projects",
            "skills": "Tech Stack",
            "education": "Education",
            "tech": "Stack",
        },
        "experience": [
            {
                "role": "Systems & Business Analyst, Vibe-Developer",
                "company": "Self-employed (Individual Entrepreneur)",
                "date": "Jul 2024 — present",
                "desc": "Multi-provider AI architecture design, FSM configurators, RAG pipelines, Python refactoring, Go REST API, multi-stage Docker. Research, development and backtesting of algorithmic trading strategies. Built MVP apps: Telegram bots, parsers, PDF generators, resume website.",
                "achievements": [
                    "Unified OpenAI-compatible architecture for 5 providers — no bot code changes when switching",
                    "AI agent with 11 tools: dual UI (CLI + Telegram) on a single core — zero code duplication",
                    "Flask→Go port: ×20 RPS at 10 MB image vs 150 MB",
                    "Transcript-to-PDF pipeline with 3 report types and base64 image embedding",
                ],
                "tech": "Python, Go, aiogram 3, FastAPI, Flask, LangChain, RAG, ChromaDB, Docker, GitHub Actions",
            },
            {
                "role": "Systems Analyst",
                "company": "Techcoredev.ru (JSC Innovative Technologies)",
                "date": "Apr 2025 — Nov 2025",
                "desc": "Insurance product management system. Full specification lifecycle, BPMN/ERD/UML/C4, AI-assisted legacy reverse engineering. Accelerated design phase by introducing AI for standard documentation fragments.",
                "achievements": [],
                "tech": "Node.js, DBeaver, MS SQL Server, Confluence, Cursor, Windsurf, PlantUML, Figma",
            },
            {
                "role": "Lead Analyst",
                "company": "Raccoonsoft.ru & Devexperts.com",
                "date": "Apr 2021 — Mar 2024",
                "desc": "Tastyworks iPad (tastytrade.com) — stocks, derivatives (options, futures), FX, crypto. Requirements elicitation, user stories, UI/UX, reverse engineering of mobile/thick/thin clients. Successful product launch.",
                "achievements": [],
                "tech": "JIRA, GitHub, Figma, Java, MindManager",
            },
            {
                "role": "Lead Analyst",
                "company": "LLC LANIT-TERCOM",
                "date": "Dec 2013 — Apr 2025",
                "desc": "Housing utilities VCKP-EIRC, Moscow Electronic School, Gazprom Neft (VEGA FEM, Digital Twin of Seismic Exploration), EMIAS (Cancer Registry), Toyota, AREA9, presale assessments (Rosatom, YOTA, Rosnedra, etc.).",
                "achievements": [],
                "tech": "Oracle, PostgreSQL, 1C, ARIS, Bizagi, Enterprise Architect, JIRA, Confluence, Kafka, Grafana",
            },
            {
                "role": "Business / Systems / Financial Analyst",
                "company": "Devexperts.com",
                "date": "Aug 2007 — May 2012",
                "desc": "ThinkOrSwim, GFT Dealbook 360, DXtrade — ATS, FX and binary options, technical analysis, dealing, mobile clients, FIX integrations, risk management, back office.",
                "achievements": [],
                "tech": "DOORS, Polarion, JIRA, Enterprise Architect, FIX protocol",
            },
            {
                "role": "Senior Business Process Analyst",
                "company": "TKB BNP Paribas Investment Partners",
                "date": "May 2012 — Mar 2013",
                "desc": "Model portfolio, Structured products, Value-at-Risk, CAPM, ATP, MTS-ATS-Robot, Data Quality, Data Mining. Specifications for Front-Middle-Back Office and Risk Management.",
                "achievements": [],
                "tech": "QUIK, MetaTrader 4/5 (+MQL), 1C, MS SQL, yEd",
            },
            {
                "role": "Senior Business Analyst",
                "company": "Deutsche Telekom IT Solutions",
                "date": "May 2013 — Dec 2013",
                "desc": "De-mail — notarial e-mail. SRS + process models (DFD, ERM, BPMN, UML) → successful preliminary design review.",
                "achievements": [],
                "tech": "Polarion, JIRA, Confluence, Enterprise Architect",
            },
            {
                "role": "Business Analyst",
                "company": "Visual Trading Systems LLC",
                "date": "Feb 2006 — Aug 2007",
                "desc": "ATS modules and Backtesting Engine for VT Trader trading platform (Capital Market Services FX).",
                "achievements": [],
                "tech": "VT Trader, MetaTrader (+MQL), MetaStock, Tradestation, Wealth-Lab",
            },
        ],
        "skills": [
            {"category": "Languages", "items": "Python 3.10+, Go 1.22, SQL, Java, Bash, MQL, TeX"},
            {"category": "AI / LLM", "items": "OpenAI API, Claude, Gemini, DeepSeek, GLM, Llama, Qwen; function calling, MCP, RAG, LangChain, ChromaDB"},
            {"category": "Frameworks", "items": "FastAPI, Flask, aiogram 3, Pydantic, Jinja2, WeasyPrint, aiohttp"},
            {"category": "Data", "items": "PostgreSQL, SQLite, Oracle, MS SQL Server, 1C, pandas, openpyxl, yfinance"},
            {"category": "ML", "items": "scikit-learn, LightGBM, PyTorch Lightning, LSTM, TFT, optuna, shap"},
            {"category": "Infrastructure", "items": "Docker, Docker Compose, Grafana Loki, GitHub Actions"},
            {"category": "BA/SA", "items": "Confluence, JIRA, BPMN, UML, C4, PlantUML, Draw.io, Figma, ARIS, Bizagi, Enterprise Architect"},
            {"category": "Standards", "items": "PMBoK, BABOK, GOST 34, IEEE 830, ISO/IEC/IEEE 29148"},
        ],
        "education": [
            {"degree": "PhD in Mathematics (Mathematical Cybernetics)", "years": "1995–1998", "place": "Saint Petersburg State University, Postgraduate, Faculty of Applied Mathematics"},
            {"degree": "MSc, Applied Mathematics", "years": "1990–1995", "place": "Saint Petersburg State University, Faculty of Applied Mathematics"},
            {"degree": "Economist, Finance and Credit", "years": "1999–2002", "place": "Saint Petersburg State University (Economics Faculty) & International Banking Institute (IBI)"},
        ],
    },
}


def load_projects():
    with open(PROJECTS_FILE, encoding="utf-8") as f:
        return json.load(f)


def build_cv_pdf(lang: str) -> bytes:
    """Generate CV PDF from site data using WeasyPrint."""
    data = CV_DATA.get(lang, CV_DATA["ru"])
    projects = load_projects()
    ts = datetime.now().strftime("%d.%m.%Y %H:%M")

    proj_list = [
        {
            "title": p["title_ru"] if lang == "ru" else p["title_en"],
            "desc": p["desc_ru"] if lang == "ru" else p["desc_en"],
            "tags": p["tags"],
            "url": p["url"],
        }
        for p in projects
    ]

    generated_at = f"Сгенерировано: {ts}" if lang == "ru" else f"Generated: {ts}"

    html_str = render_template(
        "cv_pdf.html",
        lang=lang,
        name=data["name"],
        subtitle=data["subtitle"],
        summary=data["summary"],
        labels=data["labels"],
        experience=data["experience"],
        projects=proj_list,
        skills=data["skills"],
        education=data["education"],
        generated_at=generated_at,
    )
    pdf_bytes = HTML(string=html_str, base_url=".").write_pdf()
    return pdf_bytes


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
