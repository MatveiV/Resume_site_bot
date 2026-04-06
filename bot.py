import asyncio
import json
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
)
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
CV_FILES = {
    "ru": os.path.join("static", "cv", "MatveiVasetsov_CV_RU.pdf"),
    "en": os.path.join("static", "cv", "MatveiVasetsov_CV_EN.pdf"),
}
CV_FALLBACK = os.path.join("static", "cv", "MatveiVasetsov_CV.pdf")
PROJECTS_FILE = "projects.json"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

TEXTS = {
    "ru": {
        "welcome": (
            "👋 Привет! Я бот-резюме <b>Матвея Васецова</b>.\n\n"
            "🎯 Системный и бизнес-аналитик · Vibe-кодер · К.ф.-м.н.\n"
            "📍 19 лет в FinTech + Python + LLM-инструменты\n\n"
            "Выбери раздел:"
        ),
        "about": (
            "👤 <b>Матвей Евгеньевич Васецов</b>\n\n"
            "Аналитик с 19-летним опытом в FinTech. Специализируюсь на трансляции бизнес-требований "
            "в архитектурные решения и MVP, проектировании высоконагруженных систем.\n\n"
            "💡 <i>Закрываю связку бизнес↔разработка: собираю требования, проектирую архитектуру "
            "и автоматизирую рутину на Python — вы экономите итерации и деньги.</i>\n\n"
            "📧 <a href='mailto:matvey_v@yahoo.com'>matvey_v@yahoo.com</a>  <i>(Yahoo)</i>\n"
            "✈️ <a href='https://t.me/matveivasetsov'>@matveivasetsov</a>  <i>(Telegram)</i>\n"
            "🐙 <a href='https://github.com/MatveiV'>github.com/MatveiV</a>  <i>(GitHub)</i>\n"
            "💼 <a href='https://www.linkedin.com/in/matvei-vasetsov-777b66a'>LinkedIn</a>"
        ),
        "projects_header": "🚀 <b>Проекты</b>\n\nВыбери категорию:",
        "experience": (
            "💼 <b>Опыт работы</b>\n\n"
            "▸ <b>07.2024 — н.в.</b> · ИП · Системный и бизнес-аналитик, Vibe-Developer\n"
            "  AI-архитектуры, RAG, MCP, Go REST API, Docker\n\n"
            "▸ <b>04.2025 — 11.2025</b> · Techcoredev.ru · Системный аналитик\n"
            "  Система управления страховыми продуктами\n\n"
            "▸ <b>04.2021 — 03.2024</b> · Raccoonsoft & Devexperts · Ведущий аналитик\n"
            "  Tastyworks iPad (tastytrade.com)\n\n"
            "▸ <b>12.2013 — 04.2025</b> · ЛАНИТ-ТЕРКОМ · Ведущий аналитик\n"
            "  ЖКХ, МЭШ, Газпром нефть, ЕМИАС, Toyota, AREA9\n\n"
            "▸ <b>08.2007 — 05.2012</b> · Devexperts.com · Финансовый аналитик\n"
            "  ThinkOrSwim, DXtrade, FIX-интеграции\n\n"
            "▸ <b>05.2012 — 03.2013</b> · TKB BNP Paribas · Старший аналитик\n"
            "  VaR, CAPM, Model portfolio, Data Quality\n\n"
            "▸ <b>05.2013 — 12.2013</b> · Deutsche Telekom IT Solutions · Старший BA\n"
            "  De-mail — нотариальный E-mail\n\n"
            "▸ <b>02.2006 — 08.2007</b> · Visual Trading Systems · Бизнес-аналитик\n"
            "  VT Trader, Backtesting Engine"
        ),
        "skills": (
            "🛠 <b>Технологии</b>\n\n"
            "<b>Языки:</b> Python 3.10+, Go 1.22, SQL, Bash, MQL\n\n"
            "<b>AI / LLM:</b> OpenAI API, Claude, Gemini, DeepSeek, LangChain, RAG, MCP, Function Calling\n\n"
            "<b>Фреймворки:</b> FastAPI, Flask, aiogram 3, ChromaDB, Pydantic, WeasyPrint\n\n"
            "<b>Данные:</b> PostgreSQL, SQLite, Oracle, MS SQL, pandas\n\n"
            "<b>ML:</b> scikit-learn, LightGBM, PyTorch, LSTM, optuna\n\n"
            "<b>Инфраструктура:</b> Docker, Docker Compose, Grafana Loki, GitHub Actions\n\n"
            "<b>BA/SA:</b> Confluence, JIRA, BPMN, UML, C4, PlantUML, Figma"
        ),
        "education": (
            "🎓 <b>Образование</b>\n\n"
            "▸ <b>1995–1998</b> · СПбГУ, аспирантура\n"
            "  К.ф.-м.н., Математическая кибернетика\n\n"
            "▸ <b>1990–1995</b> · СПбГУ\n"
            "  Математик, Прикладная математика\n\n"
            "▸ <b>1999–2002</b> · СПбГУ + МБИ\n"
            "  Экономист, Финансы и кредит"
        ),
        "cv_caption": "📄 Резюме Матвея Васецова (RU)",
        "cv_not_found": "⚠️ Файл резюме не найден на сервере.",
        "lang_switched": "🇬🇧 Switched to English",
        "btn_about": "👤 Обо мне",
        "btn_projects": "🚀 Проекты",
        "btn_experience": "💼 Опыт",
        "btn_skills": "🛠 Стек",
        "btn_education": "🎓 Образование",
        "btn_cv": "📄 Скачать резюме (RU)",
        "btn_lang": "🇬🇧 English",
        "btn_back": "◀ Назад",
        "btn_ai": "🤖 AI / LLM",
        "btn_infra": "⚙️ Инфраструктура",
        "btn_ml": "📈 ML / Finance",
        "proj_link_label": "🐙 GitHub",
    },
    "en": {
        "welcome": (
            "👋 Hi! I'm the resume bot of <b>Matvei Vasetsov</b>.\n\n"
            "🎯 Systems & Business Analyst · Vibe-Coder · PhD in Mathematics\n"
            "📍 19 years in FinTech + Python + LLM tools\n\n"
            "Choose a section:"
        ),
        "about": (
            "👤 <b>Matvei Evgenyevich Vasetsov</b>\n\n"
            "Analyst with 19 years of experience in FinTech. I specialise in translating business requirements "
            "into architectural decisions and MVPs, and in designing high-load systems.\n\n"
            "💡 <i>I bridge the business↔engineering gap: gather requirements, design architecture, "
            "and automate routine work in Python — saving you iterations and money.</i>\n\n"
            "📧 <a href='mailto:matvey_v@yahoo.com'>matvey_v@yahoo.com</a>  <i>(Yahoo)</i>\n"
            "✈️ <a href='https://t.me/matveivasetsov'>@matveivasetsov</a>  <i>(Telegram)</i>\n"
            "🐙 <a href='https://github.com/MatveiV'>github.com/MatveiV</a>  <i>(GitHub)</i>\n"
            "💼 <a href='https://www.linkedin.com/in/matvei-vasetsov-777b66a'>LinkedIn</a>"
        ),
        "projects_header": "🚀 <b>Projects</b>\n\nChoose a category:",
        "experience": (
            "💼 <b>Work Experience</b>\n\n"
            "▸ <b>Jul 2024 — present</b> · Self-employed · Systems & Business Analyst, Vibe-Developer\n"
            "  AI architectures, RAG, MCP, Go REST API, Docker\n\n"
            "▸ <b>Apr 2025 — Nov 2025</b> · Techcoredev.ru · Systems Analyst\n"
            "  Insurance product management system\n\n"
            "▸ <b>Apr 2021 — Mar 2024</b> · Raccoonsoft & Devexperts · Lead Analyst\n"
            "  Tastyworks iPad (tastytrade.com)\n\n"
            "▸ <b>Dec 2013 — Apr 2025</b> · LANIT-TERCOM · Lead Analyst\n"
            "  Housing utilities, Moscow Electronic School, Gazprom Neft, EMIAS, Toyota, AREA9\n\n"
            "▸ <b>Aug 2007 — May 2012</b> · Devexperts.com · Financial Analyst\n"
            "  ThinkOrSwim, DXtrade, FIX integrations\n\n"
            "▸ <b>May 2012 — Mar 2013</b> · TKB BNP Paribas · Senior Analyst\n"
            "  VaR, CAPM, Model portfolio, Data Quality\n\n"
            "▸ <b>May 2013 — Dec 2013</b> · Deutsche Telekom IT Solutions · Senior BA\n"
            "  De-mail — notarial e-mail service\n\n"
            "▸ <b>Feb 2006 — Aug 2007</b> · Visual Trading Systems · Business Analyst\n"
            "  VT Trader, Backtesting Engine"
        ),
        "skills": (
            "🛠 <b>Tech Stack</b>\n\n"
            "<b>Languages:</b> Python 3.10+, Go 1.22, SQL, Bash, MQL\n\n"
            "<b>AI / LLM:</b> OpenAI API, Claude, Gemini, DeepSeek, LangChain, RAG, MCP, Function Calling\n\n"
            "<b>Frameworks:</b> FastAPI, Flask, aiogram 3, ChromaDB, Pydantic, WeasyPrint\n\n"
            "<b>Data:</b> PostgreSQL, SQLite, Oracle, MS SQL, pandas\n\n"
            "<b>ML:</b> scikit-learn, LightGBM, PyTorch, LSTM, optuna\n\n"
            "<b>Infrastructure:</b> Docker, Docker Compose, Grafana Loki, GitHub Actions\n\n"
            "<b>BA/SA:</b> Confluence, JIRA, BPMN, UML, C4, PlantUML, Figma"
        ),
        "education": (
            "🎓 <b>Education</b>\n\n"
            "▸ <b>1995–1998</b> · Saint Petersburg State University, Postgraduate\n"
            "  PhD in Mathematics (Mathematical Cybernetics)\n\n"
            "▸ <b>1990–1995</b> · Saint Petersburg State University\n"
            "  MSc, Applied Mathematics\n\n"
            "▸ <b>1999–2002</b> · SPbSU + International Banking Institute\n"
            "  Economist, Finance and Credit"
        ),
        "cv_caption": "📄 Matvei Vasetsov's Resume (EN)",
        "cv_not_found": "⚠️ CV file not found on the server.",
        "lang_switched": "🇷🇺 Переключено на русский",
        "btn_about": "👤 About Me",
        "btn_projects": "🚀 Projects",
        "btn_experience": "💼 Experience",
        "btn_skills": "🛠 Stack",
        "btn_education": "🎓 Education",
        "btn_cv": "📄 Download CV (EN)",
        "btn_lang": "🇷🇺 Русский",
        "btn_back": "◀ Back",
        "btn_ai": "🤖 AI / LLM",
        "btn_infra": "⚙️ Infrastructure",
        "btn_ml": "📈 ML / Finance",
        "proj_link_label": "🐙 GitHub",
    }
}

user_lang: dict[int, str] = {}


def get_lang(uid: int) -> str:
    return user_lang.get(uid, "ru")


def t(uid: int, key: str) -> str:
    return TEXTS[get_lang(uid)][key]


def main_kb(uid: int) -> InlineKeyboardMarkup:
    tx = TEXTS[get_lang(uid)]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=tx["btn_about"], callback_data="about"),
         InlineKeyboardButton(text=tx["btn_projects"], callback_data="projects")],
        [InlineKeyboardButton(text=tx["btn_experience"], callback_data="experience"),
         InlineKeyboardButton(text=tx["btn_skills"], callback_data="skills")],
        [InlineKeyboardButton(text=tx["btn_education"], callback_data="education"),
         InlineKeyboardButton(text=tx["btn_cv"], callback_data="cv")],
        [InlineKeyboardButton(text=tx["btn_lang"], callback_data="toggle_lang")],
    ])


def back_kb(uid: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(uid, "btn_back"), callback_data="back")]
    ])


def projects_kb(uid: int) -> InlineKeyboardMarkup:
    tx = TEXTS[get_lang(uid)]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=tx["btn_ai"], callback_data="proj_ai")],
        [InlineKeyboardButton(text=tx["btn_infra"], callback_data="proj_infra")],
        [InlineKeyboardButton(text=tx["btn_ml"], callback_data="proj_ml")],
        [InlineKeyboardButton(text=tx["btn_back"], callback_data="back")],
    ])


def load_projects() -> list:
    with open(PROJECTS_FILE, encoding="utf-8") as f:
        return json.load(f)


def format_projects(projects: list, category: str, lang: str) -> str:
    cat_map = {"ai": "AI / LLM", "infra": "Infrastructure", "ml": "ML / Finance"}
    cat = cat_map.get(category, "")
    filtered = [p for p in projects if p["category"] == cat]
    lines = []
    for p in filtered:
        title = p["title_ru"] if lang == "ru" else p["title_en"]
        desc = p["desc_ru"] if lang == "ru" else p["desc_en"]
        tags = " · ".join(p["tags"][:4])
        lines.append(
            f"▸ <b>{title}</b>\n"
            f"  {desc}\n"
            f"  <i>{tags}</i>\n"
            f"  🐙 <a href='{p['url']}'>{p['url'].replace('https://github.com/', '')}</a>"
        )
    return "\n\n".join(lines) if lines else "—"


def get_cv_file(uid: int) -> tuple[str, str]:
    """Returns (filepath, filename) for current user language."""
    lang = get_lang(uid)
    path = CV_FILES.get(lang, CV_FILES["ru"])
    if not os.path.exists(path):
        path = CV_FALLBACK
    suffix = "RU" if lang == "ru" else "EN"
    return path, f"MatveiVasetsov_CV_{suffix}.pdf"


@dp.message(CommandStart())
async def cmd_start(message: Message):
    uid = message.from_user.id
    await message.answer(t(uid, "welcome"), reply_markup=main_kb(uid), parse_mode="HTML")


@dp.message(Command("help"))
async def cmd_help(message: Message):
    uid = message.from_user.id
    await message.answer(t(uid, "welcome"), reply_markup=main_kb(uid), parse_mode="HTML")


@dp.callback_query(F.data == "back")
async def cb_back(call: CallbackQuery):
    uid = call.from_user.id
    await call.message.edit_text(t(uid, "welcome"), reply_markup=main_kb(uid), parse_mode="HTML")


@dp.callback_query(F.data == "toggle_lang")
async def cb_lang(call: CallbackQuery):
    uid = call.from_user.id
    new_lang = "en" if get_lang(uid) == "ru" else "ru"
    user_lang[uid] = new_lang
    await call.answer(TEXTS[new_lang]["lang_switched"])
    await call.message.edit_text(t(uid, "welcome"), reply_markup=main_kb(uid), parse_mode="HTML")


@dp.callback_query(F.data == "about")
async def cb_about(call: CallbackQuery):
    uid = call.from_user.id
    await call.message.edit_text(
        t(uid, "about"), reply_markup=back_kb(uid),
        parse_mode="HTML", disable_web_page_preview=True
    )


@dp.callback_query(F.data == "experience")
async def cb_experience(call: CallbackQuery):
    uid = call.from_user.id
    await call.message.edit_text(t(uid, "experience"), reply_markup=back_kb(uid), parse_mode="HTML")


@dp.callback_query(F.data == "skills")
async def cb_skills(call: CallbackQuery):
    uid = call.from_user.id
    await call.message.edit_text(t(uid, "skills"), reply_markup=back_kb(uid), parse_mode="HTML")


@dp.callback_query(F.data == "education")
async def cb_education(call: CallbackQuery):
    uid = call.from_user.id
    await call.message.edit_text(t(uid, "education"), reply_markup=back_kb(uid), parse_mode="HTML")


@dp.callback_query(F.data == "projects")
async def cb_projects(call: CallbackQuery):
    uid = call.from_user.id
    await call.message.edit_text(t(uid, "projects_header"), reply_markup=projects_kb(uid), parse_mode="HTML")


@dp.callback_query(F.data.startswith("proj_"))
async def cb_project_cat(call: CallbackQuery):
    uid = call.from_user.id
    cat = call.data.replace("proj_", "")
    lang = get_lang(uid)
    projects = load_projects()
    text = format_projects(projects, cat, lang)
    await call.message.edit_text(
        text, reply_markup=back_kb(uid),
        parse_mode="HTML", disable_web_page_preview=True
    )


@dp.callback_query(F.data == "cv")
async def cb_cv(call: CallbackQuery):
    uid = call.from_user.id
    cv_path, cv_filename = get_cv_file(uid)
    if not os.path.exists(cv_path):
        await call.answer(t(uid, "cv_not_found"), show_alert=True)
        return
    await call.answer()
    await call.message.answer_document(
        FSInputFile(cv_path, filename=cv_filename),
        caption=t(uid, "cv_caption"),
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
