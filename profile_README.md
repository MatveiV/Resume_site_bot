# Матвей Евгеньевич Васецов

**Системный и бизнес-аналитик · Vibe-кодер · Кандидат физико-математических наук**

[![Yahoo](https://img.shields.io/badge/Yahoo-6001D2?style=flat&logo=yahoo&logoColor=white)](mailto:matvey_v@yahoo.com) matvey_v@yahoo.com &nbsp;·&nbsp; 📱 +7 921 900-86-18 &nbsp;·&nbsp; [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat&logo=telegram&logoColor=white)](https://t.me/matveivasetsov) [@matveivasetsov](https://t.me/matveivasetsov) &nbsp;·&nbsp; [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/MatveiV) [MatveiV](https://github.com/MatveiV) &nbsp;·&nbsp; [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matvei-vasetsov-777b66a)

🇬🇧 [English version](README_EN.md)

---

> *Торговая платформа, расчётная система или AI-агент под ваш процесс: 19 лет в FinTech + Python + LLM-инструменты → MVP, который не нужно переписывать после первого релиза.*

---

## Кто я

Аналитик с 19-летним опытом в FinTech. Специализируюсь на трансляции бизнес-требований в архитектурные решения и MVP, проектировании высоконагруженных систем — торговых платформ и расчётных систем. Нацелен на измеримый бизнес-результат через глубокий анализ и эффективную коммуникацию между бизнесом и разработкой.

Разработчики делают не то, а аналитика нет? Закрываю связку бизнес↔разработка: собираю требования, проектирую архитектуру и автоматизирую рутину на Python — вы экономите итерации и деньги.

---

## Проекты

### AI / LLM / Боты

- **[Resume Site + Telegram Bot](https://github.com/MatveiV/Resume_site_bot)** — сайт-резюме в стиле Apple (Flask, анимации, адаптивность) + Telegram-бот (aiogram 3) с двуязычным интерфейсом RU/EN, скачиванием PDF-резюме с timestamp, фильтрацией проектов и единой базой projects.json.
- **[MultiTools AI Agent Bot](https://github.com/MatveiV/MultiTools_AI_Agent_Bot)** — Telegram-бот с 5 AI-провайдерами, 8 ролями, генерацией изображений/видео, памятью диалога и подсчётом стоимости в рублях. Документация: 8 Mermaid-диаграмм (C4, BPMN, UML).
- **[ShortLongMemory Bots](https://github.com/MatveiV/ShortLongMemory_Bots)** — Telegram-боты с короткой (deque) и долгой (RAG + ChromaDB) памятью. FSM-конфигуратор, 3 AI-провайдера, 16+ моделей.
- **[Local AI Agent Bot](https://github.com/MatveiV/Local_AI_Agent_Bot)** — CLI и Telegram AI-агент с OpenAI function calling и 11 инструментами (поиск, погода, крипта, QR, PDF/DOCX, HTTP, терминал). 3 провайдера, 13+ моделей.
- **[Product MCP Bot](https://github.com/MatveiV/Product_MCP_Bot)** — MCP-сервер (FastAPI) + Telegram-бот с LLM tool calling. 10 инструментов: каталог товаров (SQLite), калькулятор, CoinGecko, RAWG, LibreTranslate.
- **[AI Client PDF Generator](https://github.com/MatveiV/AI_Client_PDF_Generator)** — система автогенерации PDF-отчётов по транскрибациям диалогов с клиентами. LLM → структурированный JSON → Jinja2 → WeasyPrint. 5 LLM-провайдеров, 4 бэкенда генерации изображений.
- **[LangChain Pipeline Generator](https://github.com/MatveiV/LangChain_Pipeline_Generator)** — автогенерация Telegram-ботов и документации (SRS, URS) по текстовому описанию через LLM-цепочки.
- **[Prompter](https://github.com/MatveiV/Prompter)** — CLI для A/B-тестирования техник промптинга (zero-shot, few-shot, CoT, role-based) с ранжированием и генерацией Markdown/DOCX-отчётов.
- **[PromptingAIbot & three_ai_comparison_bot](https://github.com/MatveiV/PromptingAIbot)** — Telegram-бот и CLI для сравнения ответов AI-моделей (GPT, Claude, Gemini, DeepSeek, GLM) через единый OpenAI-совместимый клиент.

### Инфраструктура и бэкенд

- **[Refactoring_MV](https://github.com/MatveiV/Refactoring_mv)** — рефакторинг Python-кода (устранение SQL-инъекций, утечек соединений, гонок потоков, небезопасного хранения паролей) с параллельной реализацией того же REST API на Go. Два Docker-образа на Docker Hub, docker-compose для совместного запуска. Документация: 7 Mermaid-диаграмм (C4 L1/L2/L3, UML классов, Sequence ×3, State, Deployment).
- **[Loki-Grafana](https://github.com/MatveiV/Loki_Grafana)** — стек централизованного логирования (Loki + Grafana) с Docker Compose и bash-скриптами автоустановки.
- **[CoinParser](https://github.com/MatveiV/CoinParser)** — парсер Telegram-канала с фильтрацией крипто-символов, интеграцией Google Sheets API и экспортом в XLSX.

### ML / Финансы

- **[ML_Fin_Notebooks](https://github.com/MatveiV/ML_Fin_Notebooks)** — ML в финансах: бэктестинг стратегий, генерация признаков (EMA, RSI, MACD), классификация, прогнозирование временных рядов (LSTM, TFT).

---

## Опыт работы

### 07.2024 — н.в. · ИП · Системный и бизнес-аналитик, vibe-developer, quantitative researcher

Проектирование мультипровайдерной AI-архитектуры, разработка FSM-конфигураторов, реализация RAG-пайплайнов, рефакторинг Python-кода, реализация REST API на Go, сборка multi-stage Docker-образов, написание архитектурной документации с Mermaid/PlantUML-диаграммами (C4, BPMN, UML).

**Ключевые достижения:**
- Единая OpenAI-совместимая архитектура для 5 разнородных провайдеров без изменения кода бота.
- AI-агент с 11 инструментами: два независимых UI (CLI и Telegram) на едином ядре без дублирования кода.
- Полный порт Flask-сервиса на Go: в 20 раз больше одновременных запросов при образе 10 МБ против 150 МБ.
- OpenAPI 3.1 спецификация для двух серверов с reusable-схемами и примерами всех ответов.
- Набор ML-стратегий для финансовых временных рядов с подтверждённым результатом на исторических данных.

---

### 04.2025 — 11.2025 · Techcoredev.ru (АО «Инновационные технологии») · Системный аналитик

**Проект:** Система управления страховыми продуктами.

Полный цикл создания спецификаций. Проектирование архитектурных решений (BPMN, ERD, UML, C4). Реверс-инжиниринг legacy-системы с применением ИИ для анализа кода и бизнес-логики.

**Достижение:** Ускорил этап проектирования за счёт внедрения ИИ для генерации типовых фрагментов документации и анализа legacy-кода.

*Node.js, DBeaver, MS SQL Server, Confluence, Cursor, Windsurf, Draw.io, PlantUML, Figma.*

---

### 04.2021 — 03.2024 · Raccoonsoft.ru & Devexperts.com · Ведущий аналитик

**Проект:** Мобильная платформа Tastyworks iPad для торговли акциями, деривативами (опционы, фьючерсы), облигациями, форекс и криптовалютами ([tastytrade.com](https://tastytrade.com)).

Выявление и моделирование требований в user stories и системных спецификациях для iPad-клиента. Участие в проектировании UI/UX, интеграций и общей архитектуры. Реверс-инжиниринг мобильной версии и толстого/тонкого клиентов. Связующее звено между бизнесом и командой разработки.

**Достижение:** Успешный вывод продукта на рынок. Сократил количество итераций на этапе разработки благодаря детальным требованиям, сформированным в Jira.

*JIRA, GitHub, Figma, Java, MindManager.*

---

### 12.2013 — 04.2025 · ООО «ЛАНИТ-ТЕРКОМ» · Ведущий аналитик

**Проекты:**

- **Услуги ЖКХ для ВЦКП-ЕИРЦ** (квитанции за услуги ЖКХ в Санкт-Петербурге) и ГИС ЖКХ. Выявление и моделирование требований, описание интеграций и ИТ-инфраструктуры, реверс-инжиниринг legacy-систем. Методологии: DFD/IDEF0/BPMN/EPC/ARIS/C4. *Oracle, PostgreSQL, 1C, PowerDesigner, ARIS, Bizagi, JIRA, Confluence, Enterprise Architect.*
- **МЭШ для ДИТ г. Москвы** (КИС ГУСОЭВ, управление олимпиадами школьников). Анализ БФТ, создание ТЗ/ЧТЗ/ППИ, UML Sequence-диаграммы, тестирование интеграций. *PostgreSQL, Java, Kafka, JIRA, Confluence, Grafana, Postman.*
- **ВЕГА ФЭМ и «Цифровой двойник сейсморазведки»** для ПАО «Газпром нефть». Адаптация систем принятия финансово-экономических и геологических решений. *ARIS, MSSQL Server, 1С.*
- **Раковый регистр в ЕМИАС** для ДИТ г. Москвы. Реверс-инжиниринг legacy-системы, создание спецификаций BPMN/UML.
- **Toyota** для ООО «Тойота Мотор Россия». Vision и ТЗ для складской подсистемы и подсистемы контроля качества.
- **AREA9** для Area9 Lyceum. Адаптация международной SaaS-платформы адаптивного обучения, локализация UI и контента.
- **Presale-оценки:** ETWeb Enterprise, ГИС ТЭК СПб, ИС для Росатом, ИС «Управление трафиком» для YOTA, ИС «Запасы» для Роснедра и др.

---

### 05.2013 — 12.2013 · Deutsche Telekom IT Solutions · Старший бизнес-аналитик

**Проект:** De-mail — нотариальный E-mail.

Анализ функциональных требований, создание описаний бизнес-процессов, спецификаций и диаграмм (DFD, ERM, BPMN, UML). Подготовленный пакет документации (SRS, модели процессов) стал основой для успешного прохождения предварительного проектирования.

*Polarion, JIRA, Confluence, Enterprise Architect.*

---

### 05.2012 — 03.2013 · TKB BNP Paribas Investment Partners · Старший аналитик бизнес-процессов

**Проекты:** Model portfolio, Структурированные продукты, Value-at-risk, CAPM, ATP, МТС-ATS-Robot, Data Quality, Data mining.

Создание спецификаций для Front-Middle-Back Office и Risk-management. Анализ и формализация математических моделей расчёта доходности и риска. Проектирование потоков данных от биржевых фидов до расчётного ядра и витрин отчётности.

*Excel, yEd, QUIK, MetaTrader 4/5 (+MQL), 1C, MS SQL.*

---

### 08.2007 — 05.2012 · Devexperts.com · Бизнес/системный/финансовый аналитик

**Проекты:** АТС, FX и бинарные опционы, технический анализ (Charting), дилинг, мобильные клиенты, интеграция по FIX, риск-менеджмент, бэк-офис. Торговые платформы: ThinkOrSwim, GFT Dealbook 360, DXtrade.

Сбор и анализ требований (на английском), проектирование и управление спецификациями для финансовых инструментов (опционы, фьючерсы, FX, ставки bet). Анализ и проектирование UI/UX. Проектирование трейдингового workflow, маржинальных расчётов и торговых отчётов. Адаптация платформы под требования брокеров и регуляторов.

*DOORS, Polarion, JIRA, Confluence, Enterprise Architect, FIX протокол.*

---

### 02.2006 — 08.2007 · Visual Trading Systems LLC · Бизнес-аналитик

**Проект:** Модули АТС и Backtesting Engine для торговой платформы VT Trader (Capital Market Services FX).

Сбор и анализ требований (на английском). Разработка АТС для VT Trader. Проектирование модуля Backtesting Engine.

*VT Trader, MetaTrader (+MQL), MetaStock, Tradestation, Wealth-Lab.*

---

## Технологии

| Категория | Стек |
|-----------|------|
| Языки | Python 3.10+, Go 1.22, SQL, Java, Bash, MQL, TeX |
| AI / LLM | OpenAI API, Claude, Gemini, DeepSeek, GLM (Z.AI), Llama, Qwen, Kimi; function calling / tool calling; MCP; промпт-инжиниринг; Cerebras WSE; HuggingFace |
| Генерация медиа | DALL·E 2/3, GPT-Image-1, FLUX.1, Kling, LTX, Sora/Sora-2, CogVideoX-3, Veo 3/3.1, Imagen 4, Pollinations.ai |
| Фреймворки | FastAPI, Flask, aiogram 3, pyTelegramBotAPI, python-telegram-bot, LangChain, openai SDK, aiohttp, ChromaDB, Pydantic, Jinja2, WeasyPrint |
| Данные | SQLite, PostgreSQL, Oracle, MS SQL Server, 1С, pandas, openpyxl, gspread, yfinance |
| ML | scikit-learn, LightGBM, PyTorch Lightning, pytorch-forecasting, optuna, shap, backtesting |
| Инфраструктура | Docker, Docker Compose, Grafana Loki, GitHub Actions |
| BA / SA инструменты | Confluence, JIRA, Redmine, Polarion, DOORS, ARIS, Bizagi, Enterprise Architect, PlantUML, Draw.io, Miro, Figma, Visio, PowerDesigner, DBeaver, Postman |
| Торговые платформы | Tastytrade, MetaTrader 4/5, DealBook 360, ThinkOrSwim, VT Trader, QUIK, Tradingview |
| Инструменты | Git/GitHub, Jupyter, LM Studio, Ollama, Cursor, Kiro, Visual Paradigm |
| Стандарты | PMBoK, BABOK, ГОСТ 34, IEEE 830, ISO/IEC/IEEE 29148 |

---

## Образование

| Годы | Учебное заведение | Степень / специальность |
|------|-------------------|------------------------|
| 1995–1998 | СПбГУ, аспирантура, факультет прикладной математики и процессов управления | К.ф.-м.н., Математическая кибернетика. Тема: «Квазисовершенные принципы оптимальности в классических кооперативных играх» |
| 1990–1995 | СПбГУ, факультет прикладной математики и процессов управления | Математик, Прикладная математика. Тема: «Теории игр: модели принятия решений в экономике» |
| 1999–2002 | СПбГУ (экономический факультет) и Международный банковский институт (IBI) | Экономист, Финансы и кредит. Тема: «Применение метода реальных опционов для оценки долгосрочных инвестиционных проектов» |

---

## Сертификаты и обучение

- 2026 — Курс «Профессия вайб-кодер» (Университет Зерокодер)
- 2026 — Курс «Интенсив по промпт-инжинирингу» (Университет Зерокодер)
- 2025 — Курс «Разработка чат-бота с AI-ассистентом» (Университет Зерокодер)
- 2025 — Frontend: Start (itlogia.ru)
- 2025 — ML в финансовом анализе (OTUS.ru)
- 2020 — Моделирование в ARIS (Luxoft-training)
- 2009 — Школа опционов (инвестиционная компания Eltra)
- 2005 — Курс финансов и международного бизнеса, Aurhus School of Business, Дания
- 2005 — TOEFL, Aurhus School of Business, Дания
- 1995 — Годичная программа по макро- и микроэкономике и финансам, Европейский университет в СПб и ЭМИАН

---

## Научные публикации и доклады

- **2025** — Доклад на конференции «Дифференциальные игры, теория управления и оптимизация» ([math.csu.ru](https://math.csu.ru/new_files/vestnik/DGCTO-2025.pdf))
- **2024** — Доклад на международной конференции «Системный анализ: моделирование и управление» ([syst2024.cs.msu.ru](https://syst2024.cs.msu.ru/SYST2024-Abstracts.pdf))
- **2020** — Статья «Система моделей построения прогрессивной шкалы подоходного налога». Вестник СПбГУ, серия 10, т. 16, вып. 1, стр. 4–18 ([dspace.spbu.ru](https://dspace.spbu.ru/bitstream/11701/17783/1/4-18.pdf))
- **2017** — Доклад «On Some Properties of Superposition of Optimality Principles on the Space of TU-Games» на конференции «Конструктивный негладкий анализ и смежные вопросы» ([ieeexplore.ieee.org](https://ieeexplore.ieee.org/document/7973949))

---

## Языки

- Русский — родной
- Английский — Upper Intermediate (B2)
