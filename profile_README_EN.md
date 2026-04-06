# Matvei Evgenyevich Vasetsov

**Systems & Business Analyst · Vibe-Coder · PhD in Mathematics**

[![Yahoo](https://img.shields.io/badge/Yahoo-6001D2?style=flat&logo=yahoo&logoColor=white)](mailto:matvey_v@yahoo.com) matvey_v@yahoo.com &nbsp;·&nbsp; 📱 +7 921 900-86-18 &nbsp;·&nbsp; [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat&logo=telegram&logoColor=white)](https://t.me/matveivasetsov) [@matveivasetsov](https://t.me/matveivasetsov) &nbsp;·&nbsp; [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/MatveiV) [MatveiV](https://github.com/MatveiV) &nbsp;·&nbsp; [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matvei-vasetsov-777b66a)

🇷🇺 [Русская версия](README.md)

---

> *Trading platform, settlement system, or AI agent for your workflow: 19 years in FinTech + Python + LLM tools → an MVP you won't need to rewrite after the first release.*

---

## About Me

Analyst with 19 years of experience in FinTech. I specialise in translating business requirements into architectural decisions and MVPs, and in designing high-load systems — trading platforms and settlement engines. Focused on measurable business outcomes through deep analysis and effective communication between business and engineering.

Developers building the wrong thing and no analyst in sight? I bridge the business↔engineering gap: gather requirements, design architecture, and automate routine work in Python — saving you iterations and money.

---

## Projects

### AI / LLM / Bots

- **[Resume Site + Telegram Bot](https://github.com/MatveiV/Resume_site_bot)** — Apple-style resume website (Flask, animations, responsive) + Telegram bot (aiogram 3) with RU/EN bilingual interface, timestamped PDF download, project filtering, and shared projects.json data source.
- **[MultiTools AI Agent Bot](https://github.com/MatveiV/MultiTools_AI_Agent_Bot)** — Telegram bot with 5 AI providers, 8 roles, image/video generation, dialogue memory, and cost tracking in RUB. Docs: 8 Mermaid diagrams (C4, BPMN, UML).
- **[ShortLongMemory Bots](https://github.com/MatveiV/ShortLongMemory_Bots)** — Telegram bots with short-term (deque) and long-term (RAG + ChromaDB) memory. FSM configurator, 3 AI providers, 16+ models.
- **[Local AI Agent Bot](https://github.com/MatveiV/Local_AI_Agent_Bot)** — CLI and Telegram AI agent with OpenAI function calling and 11 tools (search, weather, crypto, QR, PDF/DOCX, HTTP, terminal). 3 providers, 13+ models.
- **[Product MCP Bot](https://github.com/MatveiV/Product_MCP_Bot)** — MCP server (FastAPI) + Telegram bot with LLM tool calling. 10 tools: product catalogue (SQLite), calculator, CoinGecko, RAWG, LibreTranslate.
- **[AI Client PDF Generator](https://github.com/MatveiV/AI_Client_PDF_Generator)** — automated PDF report generation from client dialogue transcriptions. Pipeline: LLM → structured JSON → Jinja2 → WeasyPrint. 5 LLM providers, 4 image-generation backends.
- **[LangChain Pipeline Generator](https://github.com/MatveiV/LangChain_Pipeline_Generator)** — auto-generation of Telegram bots and documentation (SRS, URS) from a text description via LLM chains.
- **[Prompter](https://github.com/MatveiV/Prompter)** — CLI for A/B testing of prompting techniques (zero-shot, few-shot, CoT, role-based) with ranking and Markdown/DOCX report generation.
- **[PromptingAIbot & three_ai_comparison_bot](https://github.com/MatveiV/PromptingAIbot)** — Telegram bot and CLI for comparing AI model responses (GPT, Claude, Gemini, DeepSeek, GLM) via a unified OpenAI-compatible client.

### Infrastructure & Backend

- **[Refactoring_MV](https://github.com/MatveiV/Refactoring_mv)** — Python code refactoring (eliminating SQL injections, connection leaks, race conditions, insecure password storage) with a parallel Go implementation of the same REST API. Two Docker images on Docker Hub, docker-compose for joint deployment. Docs: 7 Mermaid diagrams (C4 L1/L2/L3, class diagram, Sequence ×3, State, Deployment).
- **[Loki-Grafana](https://github.com/MatveiV/Loki_Grafana)** — centralised logging stack (Loki + Grafana) with Docker Compose and automated bash install scripts.
- **[CoinParser](https://github.com/MatveiV/CoinParser)** — Telegram channel parser with crypto-symbol filtering, Google Sheets API integration, and XLSX export.

### ML / Finance

- **[ML_Fin_Notebooks](https://github.com/MatveiV/ML_Fin_Notebooks)** — ML in finance: strategy backtesting, feature engineering (EMA, RSI, MACD), classification, time-series forecasting (LSTM, TFT).

---

## Work Experience

### Jul 2024 — Present · Self-employed (IE) · Systems & Business Analyst, Vibe-Developer, Quantitative Researcher

Designing multi-provider AI architectures, building FSM configurators, implementing RAG pipelines, refactoring Python code, building REST APIs in Go, assembling multi-stage Docker images, writing architectural documentation with Mermaid/PlantUML diagrams (C4, BPMN, UML).

**Key achievements:**
- Unified OpenAI-compatible architecture for 5 heterogeneous providers — no bot code changes required when switching.
- AI agent with 11 tools: two independent UIs (CLI and Telegram) on a single core with zero code duplication.
- Full port of a Flask service to Go: 20× more concurrent requests at a 10 MB image vs 150 MB for Python.
- OpenAPI 3.1 specification for two servers with reusable schemas and response examples.
- Set of ML trading strategies for financial time series with confirmed results on historical data.

---

### Apr 2025 — Nov 2025 · Techcoredev.ru (JSC Innovative Technologies) · Systems Analyst

**Project:** Insurance product management system.

Full specification lifecycle. Architectural design using BPMN, ERD, UML, C4. Legacy system reverse engineering with AI-assisted code and business-logic analysis.

**Achievement:** Accelerated the design phase by introducing AI for generating standard documentation fragments and analysing legacy code.

*Node.js, DBeaver, MS SQL Server, Confluence, Cursor, Windsurf, Draw.io, PlantUML, Figma.*

---

### Apr 2021 — Mar 2024 · Raccoonsoft.ru & Devexperts.com · Lead Analyst

**Project:** Tastyworks iPad mobile trading platform for stocks, derivatives (options, futures), bonds, FX, and crypto ([tastytrade.com](https://tastytrade.com)).

Requirements elicitation and modelling in user stories and system specifications for the iPad client. Participation in UI/UX, integration, and overall architecture design. Reverse engineering of the mobile, thick, and thin clients. Bridge between business stakeholders (trader representatives) and the development team.

**Achievement:** Successful product launch. Reduced the number of development iterations through detailed requirements written directly in Jira rather than Confluence.

*JIRA, GitHub, Figma, Java, MindManager.*

---

### Dec 2013 — Apr 2025 · LANIT-TERCOM LLC · Lead Analyst

**Projects:**

- **Housing & Utilities Services for VCKP-EIRC** (utility bills in Saint Petersburg) and GIS Housing. Requirements elicitation and modelling, integration and IT-infrastructure descriptions, legacy system reverse engineering. Methodologies: DFD/IDEF0/BPMN/EPC/ARIS/C4. *Oracle, PostgreSQL, 1C, PowerDesigner, ARIS, Bizagi, JIRA, Confluence, Enterprise Architect.*
- **Moscow Electronic School (MES) for Moscow DIT** (KIS GUSOEV, school olympiad management). BFT analysis, TOR/detailed TOR/PPP creation, UML Sequence diagrams, integration testing. *PostgreSQL, Java, Kafka, JIRA, Confluence, Grafana, Postman.*
- **VEGA FEM and "Digital Twin of Seismic Exploration"** for Gazprom Neft PJSC. Adaptation of financial-economic and geological decision-support systems. *ARIS, MSSQL Server, 1C.*
- **Cancer Registry in EMIAS** for Moscow DIT. Legacy system reverse engineering, BPMN/UML specification authoring.
- **Toyota** for Toyota Motor Russia LLC. Vision and TOR for warehouse and quality-control subsystems.
- **AREA9** for Area9 Lyceum. Adaptation of an international adaptive-learning SaaS platform, full UI and content localisation.
- **Presale assessments:** ETWeb Enterprise, GIS TEK SPb, IS for Rosatom, Traffic Management IS for YOTA, Reserves IS for Rosnedra, and others.

---

### May 2013 — Dec 2013 · Deutsche Telekom IT Solutions · Senior Business Analyst

**Project:** De-mail — notarial e-mail service.

Functional requirements analysis, business process descriptions, specifications, and diagrams (DFD, ERM, BPMN, UML). The comprehensive documentation package (SRS, process models) I prepared became the foundation for a successful preliminary design review.

*Polarion, JIRA, Confluence, Enterprise Architect.*

---

### May 2012 — Mar 2013 · TKB BNP Paribas Investment Partners · Senior Business Process Analyst

**Projects:** Model portfolio, Structured products, Value-at-Risk, CAPM, ATP, MTS-ATS-Robot, Data Quality, Data Mining.

Specifications for Front-Middle-Back Office and Risk Management software. Analysis and formalisation of mathematical models for yield and risk calculation. Data flow design from market feeds (exchange feeds, 1C) to the calculation engine and reporting data marts.

**Achievement:** The requirements package underpinned a successful software upgrade.

*Excel, yEd, QUIK, MetaTrader 4/5 (+MQL), 1C, MS SQL.*

---

### Aug 2007 — May 2012 · Devexperts.com · Business / Systems / Financial Analyst

**Projects:** ATS (algorithmic trading strategies), FX and binary options, technical analysis (Charting), dealing, mobile clients, FIX integration, risk management, back office, UI localisation. Trading platforms: ThinkOrSwim, GFT Dealbook 360, DXtrade.

Requirements gathering and analysis (in English), specification design and management for financial instruments (options, futures, FX, binary options, bet). UI/UX analysis and design. Trading workflow design, margin calculation descriptions, and trading report specifications. Platform adaptation for specific broker and regulatory requirements.

**Achievement:** My specifications were the key reference document for the development team. The platform launched successfully and handled peak loads.

*DOORS, Polarion, JIRA, Confluence, Enterprise Architect, FIX protocol.*

---

### Feb 2006 — Aug 2007 · Visual Trading Systems LLC · Business Analyst

**Project:** ATS modules and Backtesting Engine for the VT Trader platform (Capital Market Services FX).

Requirements gathering and analysis (in English). ATS development for VT Trader based on user forum requests. Backtesting Engine module design.

**Achievement:** Successful platform enhancement launch.

*VT Trader, MetaTrader (+MQL), MetaStock, Tradestation, Wealth-Lab.*

---

## Tech Stack

| Category | Stack |
|----------|-------|
| Languages | Python 3.10+, Go 1.22, SQL, Java, Bash, MQL, TeX |
| AI / LLM | OpenAI API, Claude, Gemini, DeepSeek, GLM (Z.AI), Llama, Qwen, Kimi; function calling / tool calling; MCP; prompt engineering; Cerebras WSE; HuggingFace Inference Providers |
| Media generation | DALL·E 2/3, GPT-Image-1, FLUX.1, Kling, LTX, Sora/Sora-2, CogVideoX-3, Veo 3/3.1, Imagen 4, Pollinations.ai |
| Frameworks | FastAPI, Flask, aiogram 3, pyTelegramBotAPI, python-telegram-bot, LangChain, openai SDK, aiohttp, ChromaDB, Pydantic, Jinja2, WeasyPrint |
| Data | SQLite, PostgreSQL, Oracle, MS SQL Server, 1C, pandas, openpyxl, gspread, yfinance |
| ML | scikit-learn, LightGBM, PyTorch Lightning, pytorch-forecasting, optuna, shap, backtesting |
| Infrastructure | Docker, Docker Compose, Grafana Loki, GitHub Actions |
| BA / SA tools | Confluence, JIRA, Redmine, Polarion, DOORS, ARIS, Bizagi, Enterprise Architect, PlantUML, Draw.io, Miro, Figma, Visio, PowerDesigner, DBeaver, Postman |
| Trading platforms | Tastytrade, MetaTrader 4/5, DealBook 360, ThinkOrSwim, VT Trader, QUIK, Tradingview |
| Dev tools | Git/GitHub, Jupyter, LM Studio, Ollama, Cursor, Kiro, Visual Paradigm |
| Standards | PMBoK, BABOK, GOST 34, IEEE 830, ISO/IEC/IEEE 29148 |

---

## Education

| Years | Institution | Degree / Specialisation |
|-------|-------------|------------------------|
| 1995–1998 | Saint Petersburg State University, Postgraduate, Faculty of Applied Mathematics and Control Processes | PhD in Mathematics (Candidate of Physical and Mathematical Sciences), Mathematical Cybernetics. Thesis: "Quasi-perfect Optimality Principles in Classical Cooperative Games" |
| 1990–1995 | Saint Petersburg State University, Faculty of Applied Mathematics and Control Processes | MSc, Applied Mathematics. Thesis: "Game Theory: Decision-Making Models in Economics" |
| 1999–2002 | Saint Petersburg State University (Economics Faculty) & International Banking Institute (IBI) | Economist, Finance and Credit. Thesis: "Application of the Real Options Method for Evaluating Long-Term Investment Projects" |

---

## Certifications & Training

- 2026 — "Vibe-Coder" professional course (Zerocoder University)
- 2026 — Prompt Engineering Intensive (Zerocoder University)
- 2025 — "AI Chatbot Development" course (Zerocoder University)
- 2025 — Frontend: Start (itlogia.ru)
- 2025 — ML in Financial Analysis (OTUS.ru)
- 2020 — ARIS Modelling (Luxoft Training)
- 2009 — Options Trading School (Eltra Investment Company)
- 2005 — Finance and International Business course, Aarhus School of Business, Denmark
- 2005 — TOEFL, Aarhus School of Business, Denmark
- 1995 — Annual programme in macro/microeconomics and finance, European University at St. Petersburg & EMIN

---

## Publications & Conference Papers

- **2025** — Paper at the conference "Differential Games, Control Theory and Optimisation" ([math.csu.ru](https://math.csu.ru/new_files/vestnik/DGCTO-2025.pdf))
- **2024** — Paper at the international conference "System Analysis: Modelling and Control" ([syst2024.cs.msu.ru](https://syst2024.cs.msu.ru/SYST2024-Abstracts.pdf))
- **2020** — Article "A System of Models for Building a Progressive Income Tax Scale". Vestnik SPbSU, Series 10, vol. 16, issue 1, pp. 4–18 ([dspace.spbu.ru](https://dspace.spbu.ru/bitstream/11701/17783/1/4-18.pdf))
- **2017** — Paper "On Some Properties of Superposition of Optimality Principles on the Space of TU-Games" at the international conference "Constructive Nonsmooth Analysis and Related Topics" ([ieeexplore.ieee.org](https://ieeexplore.ieee.org/document/7973949))

---

## Languages

- Russian — native
- English — Upper Intermediate (B2)
