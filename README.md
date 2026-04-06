# Resume Site + Telegram Bot

Apple-style resume website (Flask) + Telegram bot (aiogram 3) with bilingual RU/EN interface, on-the-fly PDF generation via WeasyPrint, and a shared `projects.json` data source.

**Repository:** [github.com/MatveiV/Resume_site_bot](https://github.com/MatveiV/Resume_site_bot)

---

## Architecture — C4 Level 1 (System Context)

```mermaid
C4Context
  title System Context — Resume Site + Telegram Bot

  Person(user_web, "Web User", "Opens the resume website in a browser")
  Person(user_tg, "Telegram User", "Chats with the resume bot")

  System(site, "Resume Website", "Apple-style SPA. Flask backend. RU/EN switch. PDF download.")
  System(bot, "Telegram Bot", "aiogram 3. RU/EN menu. Sends generated PDF.")

  System_Ext(telegram, "Telegram API", "Delivers messages and files to the user")
  System_Ext(github, "GitHub", "Hosts source code and profile READMEs")
  System_Ext(fonts, "Google Fonts", "Serves Inter typeface to the browser")

  Rel(user_web, site, "Browses resume, downloads CV PDF", "HTTPS")
  Rel(user_tg, telegram, "Sends commands", "HTTPS")
  Rel(telegram, bot, "Forwards updates", "HTTPS / Webhook or polling")
  Rel(bot, telegram, "Sends messages and PDF files", "HTTPS")
  Rel(site, fonts, "Loads Inter font", "HTTPS")
```

---

## Architecture — C4 Level 2 (Container)

```mermaid
C4Container
  title Container Diagram — Resume Site + Telegram Bot

  Person(user_web, "Web User")
  Person(user_tg, "Telegram User")

  System_Boundary(app, "Resume Application") {
    Container(flask, "Flask Web App", "Python / Flask 3", "Serves HTML SPA, /api/projects, /download-cv")
    Container(bot_proc, "Telegram Bot Process", "Python / aiogram 3", "Handles commands, sends PDF via Telegram API")
    Container(cv_gen, "cv_generator.py", "Python / Jinja2 + WeasyPrint", "Renders cv_pdf.html template and produces PDF bytes")
    ContainerDb(projects_json, "projects.json", "JSON file", "Shared list of projects (title, desc, tags, url) in RU and EN")
    Container(static, "Static Assets", "HTML / CSS / JS", "SPA template, i18n, scroll reveal, project filter")
  }

  System_Ext(telegram_api, "Telegram Bot API", "External")
  System_Ext(fonts, "Google Fonts", "External")

  Rel(user_web, flask, "HTTP GET /", "HTTPS")
  Rel(flask, static, "Renders index.html + serves CSS/JS")
  Rel(flask, projects_json, "Reads on /api/projects")
  Rel(flask, cv_gen, "Calls build_cv_pdf(lang) on /download-cv")
  Rel(static, fonts, "Loads Inter", "HTTPS")

  Rel(user_tg, telegram_api, "Sends /start, taps buttons", "HTTPS")
  Rel(telegram_api, bot_proc, "Delivers updates (polling)", "HTTPS")
  Rel(bot_proc, projects_json, "Reads project list")
  Rel(bot_proc, cv_gen, "Calls build_cv_pdf(lang)")
  Rel(bot_proc, telegram_api, "Sends text messages and PDF", "HTTPS")
  Rel(cv_gen, projects_json, "Reads projects for PDF")
```

---

## Architecture — C4 Level 3 (Component — cv_generator)

```mermaid
C4Component
  title Component Diagram — cv_generator.py

  Container_Boundary(gen, "cv_generator.py") {
    Component(data, "CV_DATA dict", "Python dict", "Full resume content in RU and EN: experience, skills, education")
    Component(loader, "load_projects()", "Python function", "Reads projects.json and returns list")
    Component(builder, "build_cv_pdf(lang)", "Python function", "Orchestrates rendering and PDF conversion")
    Component(jinja, "Jinja2 Environment", "jinja2.Environment", "Loads cv_pdf.html from templates/ directory")
    Component(weasy, "WeasyPrint HTML", "weasyprint.HTML", "Converts rendered HTML string to PDF bytes")
  }

  ContainerDb(projects_json, "projects.json", "JSON file")
  Container(tmpl, "cv_pdf.html", "Jinja2 template", "PDF layout: header, experience, projects, skills, education")

  Rel(builder, data, "Reads resume content for given lang")
  Rel(builder, loader, "Gets project list")
  Rel(loader, projects_json, "Reads file")
  Rel(builder, jinja, "Renders template with context")
  Rel(jinja, tmpl, "Loads template")
  Rel(builder, weasy, "Passes rendered HTML")
  Rel(weasy, builder, "Returns PDF bytes")
```

---

## Sequence — Web User Downloads CV

```mermaid
sequenceDiagram
  actor User as Web User
  participant Browser
  participant Flask as Flask (app.py)
  participant Gen as cv_generator.py
  participant JSON as projects.json

  User->>Browser: Click "Download CV" (lang=en)
  Browser->>Flask: GET /download-cv?lang=en
  Flask->>Gen: build_cv_pdf("en")
  Gen->>JSON: load_projects()
  JSON-->>Gen: project list
  Gen->>Gen: render cv_pdf.html via Jinja2
  Gen->>Gen: WeasyPrint → PDF bytes
  Gen-->>Flask: PDF bytes
  Flask-->>Browser: MatveiVasetsov_CV_EN_20260406_153042.pdf
  Browser-->>User: Save file dialog
```

---

## Sequence — Telegram User Downloads CV

```mermaid
sequenceDiagram
  actor User as Telegram User
  participant TG as Telegram API
  participant Bot as bot.py (aiogram 3)
  participant Gen as cv_generator.py
  participant JSON as projects.json

  User->>TG: Tap "📄 Download CV (EN)"
  TG->>Bot: CallbackQuery data="cv"
  Bot->>Gen: build_cv_pdf("en")
  Gen->>JSON: load_projects()
  JSON-->>Gen: project list
  Gen->>Gen: Jinja2 render + WeasyPrint
  Gen-->>Bot: PDF bytes
  Bot->>TG: answer_document(BufferedInputFile, filename=CV_EN_<timestamp>.pdf)
  TG-->>User: PDF file in chat
```

---

## Sequence — Language Switch (Website)

```mermaid
sequenceDiagram
  actor User as Web User
  participant Browser
  participant JS as main.js (i18n)
  participant API as Flask /api/projects

  User->>Browser: Click "EN" button
  Browser->>JS: langToggle click → applyLang("en")
  JS->>JS: Update all [data-i18n] elements
  JS->>JS: Render exp1Achievements list in EN
  JS->>JS: Update CV download links (?lang=en)
  JS->>JS: localStorage.setItem("lang","en")
  JS->>JS: renderProjects(currentFilter)
  Note over JS: Projects re-rendered with EN titles/descs
```

---

## Class Diagram — Key Modules

```mermaid
classDiagram
  class app_py {
    +index() Response
    +api_projects() JSON
    +download_cv() Response
  }

  class bot_py {
    -user_lang: dict
    +cmd_start(message)
    +cb_back(call)
    +cb_lang(call)
    +cb_about(call)
    +cb_projects(call)
    +cb_project_cat(call)
    +cb_experience(call)
    +cb_skills(call)
    +cb_education(call)
    +cb_cv(call)
    -get_lang(uid) str
    -main_kb(uid) InlineKeyboardMarkup
    -format_projects(projects, cat, lang) str
  }

  class cv_generator_py {
    +CV_DATA: dict
    +build_cv_pdf(lang) bytes
    -load_projects() list
    -_jinja_env: Environment
  }

  class projects_json {
    +id: int
    +title_ru: str
    +title_en: str
    +desc_ru: str
    +desc_en: str
    +tags: list
    +category: str
    +url: str
  }

  app_py --> cv_generator_py : build_cv_pdf()
  bot_py --> cv_generator_py : build_cv_pdf()
  cv_generator_py --> projects_json : load_projects()
  app_py --> projects_json : load_projects()
```

---

## Project Structure

```
Resume_site_bot/
├── app.py               # Flask backend — routes: /, /api/projects, /download-cv
├── bot.py               # Telegram bot — aiogram 3, inline keyboards, i18n
├── cv_generator.py      # Standalone PDF generator (Jinja2 + WeasyPrint, no Flask context)
├── projects.json        # Shared project database (RU + EN, 12 projects)
├── requirements.txt
├── .env.example         # BOT_TOKEN placeholder
├── .gitignore
├── templates/
│   ├── index.html       # Single-page resume site (Apple dark theme)
│   └── cv_pdf.html      # Jinja2 template for PDF generation
└── static/
    ├── css/style.css    # Dark glassmorphism theme, animations, responsive
    ├── js/main.js       # i18n engine, project filter, scroll reveal, lang persistence
    └── cv/              # (optional) place static PDF fallbacks here
```

---

## Quick Start

```bash
# 1. Activate virtual environment
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux / macOS

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env — set BOT_TOKEN=<your token from @BotFather>

# 4. Run the website
python app.py
# → http://localhost:5000

# 5. Run the bot (separate terminal, venv activated)
python bot.py
```

---

## Feature Matrix

| Feature | Website | Telegram Bot |
|---------|---------|--------------|
| RU / EN language switch | ✅ Button in nav, persisted in localStorage | ✅ Inline keyboard button |
| Generate CV PDF on-the-fly | ✅ `/download-cv?lang=ru\|en` | ✅ Sends `BufferedInputFile` |
| Timestamp in CV filename | ✅ `CV_RU_20260406_153000.pdf` | ✅ Same format |
| Project list from JSON | ✅ `/api/projects` → JS render | ✅ Category menu |
| Filter projects by category | ✅ Filter bar (AI/LLM, Infra, ML) | ✅ 3 category buttons |
| Direct GitHub repo links | ✅ Per project card | ✅ Per project in list |
| Brand icons (Yahoo/TG/GH/LI) | ✅ SVG inline in contacts | ✅ Emoji + label |
| Scroll reveal animations | ✅ IntersectionObserver | — |
| Responsive layout | ✅ CSS Grid, mobile nav hidden | — |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Web backend | Python 3.10+, Flask 3.x |
| Telegram bot | aiogram 3.x, python-dotenv |
| PDF generation | WeasyPrint, Jinja2 |
| Frontend | Vanilla HTML / CSS / JS, Inter font |
| Data | JSON (projects.json) |
| Diagrams | Mermaid (C4, Sequence, Class) |

---

## Adding / Editing Projects

Edit `projects.json` — no server restart needed. Schema:

```json
{
  "id": 13,
  "title_ru": "Название проекта",
  "title_en": "Project Title",
  "desc_ru": "Описание на русском.",
  "desc_en": "Description in English.",
  "tags": ["Python", "FastAPI"],
  "category": "AI / LLM",
  "url": "https://github.com/MatveiV/repo-name"
}
```

Valid categories: `AI / LLM` · `Infrastructure` · `ML / Finance`
