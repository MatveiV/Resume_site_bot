// ===== i18n =====
const i18n = {
  ru: {
    page_title: "Матвей Васецов — Аналитик",
    nav_about: "Обо мне", nav_projects: "Проекты", nav_experience: "Опыт",
    nav_skills: "Стек", nav_contact: "Контакты", nav_cv: "Скачать CV",
    hero_name: "Матвей<br>Васецов",
    hero_eyebrow: "Системный и бизнес-аналитик · Vibe-кодер · К.ф.-м.н.",
    hero_tagline: "19 лет в FinTech + Python + LLM-инструменты →<br>MVP, который не нужно переписывать после первого релиза.",
    hero_cta_projects: "Смотреть проекты", hero_cta_cv: "Скачать резюме",
    utp1_title: "Бизнес ↔ Разработка",
    utp1_desc: "Закрываю связку: собираю требования, проектирую архитектуру и автоматизирую рутину на Python — вы экономите итерации и деньги.",
    utp2_title: "FinTech-экспертиза",
    utp2_desc: "Торговые платформы, расчётные системы, риск-менеджмент — 19 лет в высоконагруженных финансовых системах.",
    utp3_title: "AI-нативный аналитик",
    utp3_desc: "LLM, RAG, MCP, function calling — применяю AI-инструменты для ускорения проектирования и разработки.",
    projects_title: "Проекты",
    filter_all: "Все", filter_infra: "Инфраструктура",
    exp_title: "Опыт работы", present: "н.в.",
    exp1_role: "ИП · Системный и бизнес-аналитик, Vibe-Developer",
    exp1_desc: "Проектирование мультипровайдерной AI-архитектуры, FSM-конфигураторы, RAG-пайплайны, рефакторинг Python, REST API на Go, multi-stage Docker, архитектурная документация. Разработка и бэктестинг алгоритмических стратегий. Создание MVP-приложений: Telegram-боты, парсеры, генераторы PDF, сайт-резюме.",
    exp1_achievements: [
      "Единая OpenAI-совместимая архитектура для 5 провайдеров без изменения кода бота",
      "AI-агент с 11 инструментами: два UI (CLI + Telegram) на едином ядре без дублирования кода",
      "Порт Flask→Go: ×20 RPS при образе 10 МБ vs 150 МБ",
      "Пайплайн транскрипция→PDF с 3 типами отчётов и base64-встраиванием изображений",
    ],
    exp2_role: "Techcoredev.ru · Системный аналитик",
    exp2_desc: "Система управления страховыми продуктами. Полный цикл спецификаций, BPMN/ERD/UML/C4, реверс-инжиниринг legacy с AI. Ускорил этап проектирования за счёт AI-генерации типовых фрагментов документации.",
    exp3_role: "Raccoonsoft & Devexperts · Ведущий аналитик",
    exp3_desc: "Tastyworks iPad (tastytrade.com) — акции, деривативы (опционы, фьючерсы), форекс, крипто. Выявление требований, user stories, UI/UX, реверс-инжиниринг мобильного/толстого/тонкого клиентов. Успешный вывод продукта на рынок.",
    exp4_role: "ЛАНИТ-ТЕРКОМ · Ведущий аналитик",
    exp4_desc: "ЖКХ ВЦКП-ЕИРЦ, МЭШ ДИТ Москвы, Газпром нефть (ВЕГА ФЭМ, Цифровой двойник сейсморазведки), ЕМИАС (Раковый регистр), Toyota, AREA9, presale-оценки (Росатом, YOTA, Роснедра и др.).",
    exp5_role: "Devexperts.com · Бизнес/системный/финансовый аналитик",
    exp5_desc: "ThinkOrSwim, GFT Dealbook 360, DXtrade — АТС, FX и бинарные опционы, технический анализ, дилинг, мобильные клиенты, FIX-интеграции, риск-менеджмент, бэк-офис.",
    exp6_role: "TKB BNP Paribas Investment Partners · Старший аналитик",
    exp6_desc: "Model portfolio, Structured products, Value-at-Risk, CAPM, ATP, MTS-ATS-Robot, Data Quality, Data Mining. Спецификации для Front-Middle-Back Office и Risk Management.",
    exp7_role: "Deutsche Telekom IT Solutions · Старший бизнес-аналитик",
    exp7_desc: "De-mail — нотариальный E-mail. SRS + модели процессов (DFD, ERM, BPMN, UML) → успешное прохождение предварительного проектирования.",
    exp8_role: "Visual Trading Systems LLC · Бизнес-аналитик",
    exp8_desc: "АТС и Backtesting Engine для торговой платформы VT Trader (Capital Market Services FX). Сбор и анализ требований на английском языке.",
    skills_title: "Технологии",
    sk_lang: "Языки", sk_frameworks: "Фреймворки", sk_data: "Данные", sk_infra: "Инфраструктура",
    edu_title: "Образование",
    edu1_title: "К.ф.-м.н., Математическая кибернетика",
    edu1_place: "СПбГУ, аспирантура, факультет прикладной математики",
    edu2_title: "Математик, Прикладная математика",
    edu2_place: "СПбГУ, факультет прикладной математики",
    edu3_title: "Экономист, Финансы и кредит",
    edu3_place: "СПбГУ (экономический факультет) и МБИ",
    contact_title: "Контакты", contact_cv: "Скачать резюме PDF",
    project_link: "GitHub →",
  },
  en: {
    page_title: "Matvei Vasetsov — Analyst",
    nav_about: "About", nav_projects: "Projects", nav_experience: "Experience",
    nav_skills: "Stack", nav_contact: "Contact", nav_cv: "Download CV",
    hero_name: "Matvei<br>Vasetsov",
    hero_eyebrow: "Systems & Business Analyst · Vibe-Coder · PhD in Mathematics",
    hero_tagline: "19 years in FinTech + Python + LLM tools →<br>an MVP you won't need to rewrite after the first release.",
    hero_cta_projects: "View Projects", hero_cta_cv: "Download CV",
    utp1_title: "Business ↔ Engineering",
    utp1_desc: "I bridge the gap: gather requirements, design architecture, and automate routine work in Python — saving you iterations and money.",
    utp2_title: "FinTech Expertise",
    utp2_desc: "Trading platforms, settlement systems, risk management — 19 years in high-load financial systems.",
    utp3_title: "AI-Native Analyst",
    utp3_desc: "LLM, RAG, MCP, function calling — I use AI tools to accelerate design and development.",
    projects_title: "Projects",
    filter_all: "All", filter_infra: "Infrastructure",
    exp_title: "Work Experience", present: "present",
    exp1_role: "Self-employed · Systems & Business Analyst, Vibe-Developer",
    exp1_desc: "Multi-provider AI architecture design, FSM configurators, RAG pipelines, Python refactoring, Go REST API, multi-stage Docker, architectural documentation. Research, development and backtesting of algorithmic trading strategies. Built MVP apps: Telegram bots, parsers, PDF generators, resume website.",
    exp1_achievements: [
      "Unified OpenAI-compatible architecture for 5 providers — no bot code changes when switching",
      "AI agent with 11 tools: dual UI (CLI + Telegram) on a single core — zero code duplication",
      "Flask→Go port: ×20 RPS at 10 MB image vs 150 MB",
      "Transcript-to-PDF pipeline with 3 report types and base64 image embedding for cross-platform rendering",
    ],
    exp2_role: "Techcoredev.ru · Systems Analyst",
    exp2_desc: "Insurance product management system. Full specification lifecycle, BPMN/ERD/UML/C4, AI-assisted legacy reverse engineering. Accelerated design phase by introducing AI for standard documentation fragments.",
    exp3_role: "Raccoonsoft & Devexperts · Lead Analyst",
    exp3_desc: "Tastyworks iPad (tastytrade.com) — stocks, derivatives (options, futures), FX, crypto. Requirements elicitation, user stories, UI/UX, reverse engineering of mobile/thick/thin clients. Successful product launch.",
    exp4_role: "LANIT-TERCOM · Lead Analyst",
    exp4_desc: "Housing utilities VCKP-EIRC, Moscow Electronic School, Gazprom Neft (VEGA FEM, Digital Twin of Seismic Exploration), EMIAS (Cancer Registry), Toyota, AREA9, presale assessments (Rosatom, YOTA, Rosnedra, etc.).",
    exp5_role: "Devexperts.com · Business / Systems / Financial Analyst",
    exp5_desc: "ThinkOrSwim, GFT Dealbook 360, DXtrade — ATS, FX and binary options, technical analysis, dealing, mobile clients, FIX integrations, risk management, back office.",
    exp6_role: "TKB BNP Paribas Investment Partners · Senior Analyst",
    exp6_desc: "Model portfolio, Structured products, Value-at-Risk, CAPM, ATP, MTS-ATS-Robot, Data Quality, Data Mining. Specifications for Front-Middle-Back Office and Risk Management.",
    exp7_role: "Deutsche Telekom IT Solutions · Senior Business Analyst",
    exp7_desc: "De-mail — notarial e-mail. SRS + process models (DFD, ERM, BPMN, UML) → successful preliminary design review.",
    exp8_role: "Visual Trading Systems LLC · Business Analyst",
    exp8_desc: "ATS modules and Backtesting Engine for VT Trader trading platform (Capital Market Services FX). Requirements gathering and analysis in English.",
    skills_title: "Tech Stack",
    sk_lang: "Languages", sk_frameworks: "Frameworks", sk_data: "Data", sk_infra: "Infrastructure",
    edu_title: "Education",
    edu1_title: "PhD in Mathematics (Mathematical Cybernetics)",
    edu1_place: "Saint Petersburg State University, Postgraduate",
    edu2_title: "MSc, Applied Mathematics",
    edu2_place: "Saint Petersburg State University",
    edu3_title: "Economist, Finance and Credit",
    edu3_place: "SPbSU (Economics Faculty) & International Banking Institute",
    contact_title: "Contact", contact_cv: "Download CV PDF",
    project_link: "GitHub →",
  }
};

let currentLang = localStorage.getItem("lang") || "ru";
let allProjects = [];

function updateCvLinks() {
  document.querySelectorAll(".cv-download-btn, #navCvBtn").forEach(el => {
    el.href = `/download-cv?lang=${currentLang}`;
  });
}

function applyLang(lang) {
  currentLang = lang;
  const t = i18n[lang];
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (t[key] !== undefined) el.innerHTML = t[key];
  });
  // render achievements list separately (can't use data-i18n on <li>)
  const ul = document.getElementById("exp1Achievements");
  if (ul && t.exp1_achievements) {
    ul.innerHTML = t.exp1_achievements.map(a => `<li>${a}</li>`).join("");
  }
  document.title = t.page_title;
  document.getElementById("langToggle").textContent = lang === "ru" ? "EN" : "RU";
  document.documentElement.lang = lang;
  updateCvLinks();
  renderProjects(currentFilter);
}

document.getElementById("langToggle").addEventListener("click", () => {
  const next = currentLang === "ru" ? "en" : "ru";
  localStorage.setItem("lang", next);
  applyLang(next);
});

// ===== PROJECTS =====
let currentFilter = "all";

async function loadProjects() {
  const res = await fetch("/api/projects");
  allProjects = await res.json();
  applyLang(currentLang); // apply correct language after data is ready
}

function renderProjects(cat) {
  currentFilter = cat;
  const grid = document.getElementById("projectsGrid");
  const t = i18n[currentLang];
  const filtered = cat === "all" ? allProjects : allProjects.filter(p => p.category === cat);

  grid.innerHTML = filtered.map(p => `
    <div class="project-card">
      <div class="project-cat">${p.category}</div>
      <h3>${currentLang === "ru" ? p.title_ru : p.title_en}</h3>
      <p>${currentLang === "ru" ? p.desc_ru : p.desc_en}</p>
      <div class="project-tags">${p.tags.map(tag => `<span class="tag">${tag}</span>`).join("")}</div>
      <a href="${p.url}" target="_blank" class="project-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
        ${t.project_link}
      </a>
    </div>
  `).join("");
}

document.getElementById("filterBar").addEventListener("click", e => {
  const btn = e.target.closest(".filter-btn");
  if (!btn) return;
  document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");
  renderProjects(btn.dataset.cat);
});

// ===== SCROLL REVEAL =====
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.style.opacity = "1";
      e.target.style.transform = "translateY(0)";
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll(".utp-card, .edu-card, .skill-group, .timeline-item, .contact-item").forEach(el => {
  el.style.opacity = "0";
  el.style.transform = "translateY(20px)";
  el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
  observer.observe(el);
});

loadProjects();
