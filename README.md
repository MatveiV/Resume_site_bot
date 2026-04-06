# Resume Site + Telegram Bot

Сайт-резюме в стиле Apple + Telegram-бот на базе единого `projects.json`.

## Структура

```
├── app.py              # Flask backend
├── bot.py              # Telegram bot (aiogram 3)
├── projects.json       # Единая база проектов
├── requirements.txt
├── .env.example
├── templates/
│   └── index.html
└── static/
    ├── css/style.css
    ├── js/main.js
    └── cv/             # Положи сюда MatveiVasetsov_CV.pdf
```

## Быстрый старт

```bash
# 1. Создать и активировать виртуальное окружение
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Настроить переменные окружения
cp .env.example .env
# Вставь токен бота в .env

# 4. Положи PDF резюме в static/cv/MatveiVasetsov_CV.pdf

# 5. Запустить сайт
python app.py

# 6. Запустить бота (в отдельном терминале)
python bot.py
```

Сайт доступен на http://localhost:5000

## Добавление проектов

Редактируй `projects.json` — изменения подхватываются без перезапуска сервера.

## Переключение языка

- Сайт: кнопка EN/RU в навигации
- Бот: кнопка 🇬🇧 English / 🇷🇺 Русский в главном меню

## Скачать резюме

- Сайт: кнопка «Скачать CV» → `/download-cv`
- Бот: кнопка «📄 Скачать резюме»
