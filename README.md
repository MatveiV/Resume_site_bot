# Resume Site + Telegram Bot

Apple-style resume website (Flask) + Telegram bot (aiogram 3) with bilingual RU/EN interface, shared `projects.json` data source, and timestamped PDF download.

**Live projects:** [github.com/MatveiV/Resume_site_bot](https://github.com/MatveiV/Resume_site_bot)

## Structure

```
├── app.py              # Flask backend
├── bot.py              # Telegram bot (aiogram 3)
├── projects.json       # Shared projects database
├── requirements.txt
├── .env.example
├── templates/
│   └── index.html      # Apple-style single-page site
└── static/
    ├── css/style.css   # Dark theme, glassmorphism, animations
    ├── js/main.js      # i18n, project filtering, scroll reveal
    └── cv/             # Place PDF resumes here:
        ├── MatveiVasetsov_CV_RU.pdf
        └── MatveiVasetsov_CV_EN.pdf
```

## Quick Start

```bash
# 1. Activate virtual environment
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux/macOS

# 2. Install dependencies (already done if venv exists)
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env — add your BOT_TOKEN

# 4. Place PDF resumes in static/cv/
#    MatveiVasetsov_CV_RU.pdf  (Russian version)
#    MatveiVasetsov_CV_EN.pdf  (English version)

# 5. Run the website
python app.py
# → http://localhost:5000

# 6. Run the bot (separate terminal)
python bot.py
```

## Features

| Feature | Website | Bot |
|---------|---------|-----|
| RU / EN language switch | ✅ Button in nav | ✅ Inline button |
| Download CV PDF | ✅ `/download-cv?lang=ru\|en` | ✅ Sends file |
| Timestamp in filename | ✅ `CV_RU_20260406_153000.pdf` | ✅ Same |
| Project filtering by category | ✅ Filter bar | ✅ Category menu |
| Direct GitHub repo links | ✅ Per project | ✅ Per project |
| Brand icons (Yahoo/TG/GH/LI) | ✅ SVG inline | ✅ Emoji + label |

## Adding / Editing Projects

Edit `projects.json` — changes are picked up without server restart. Each entry:

```json
{
  "id": 1,
  "title_ru": "...", "title_en": "...",
  "desc_ru": "...",  "desc_en": "...",
  "tags": ["Python", "Flask"],
  "category": "AI / LLM",
  "url": "https://github.com/MatveiV/repo-name"
}
```

Categories: `AI / LLM`, `Infrastructure`, `ML / Finance`

## Tech Stack

- **Backend:** Python 3.10+, Flask 3.x
- **Bot:** aiogram 3.x, python-dotenv
- **Frontend:** Vanilla HTML/CSS/JS (no frameworks), Inter font, CSS animations
- **Data:** JSON file (projects.json)
