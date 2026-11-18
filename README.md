# AI Data Readiness Auditor (with Retail Validation Extension)

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit%20Cloud-FF4B4B?logo=streamlit&logoColor=white)](https://ai-data-readiness-auditor-g94hkbe2thkhwu9yrv3l5a.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![pandas](https://img.shields.io/badge/pandas-Data-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Charts-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/python/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Local-first](https://img.shields.io/badge/Local--first-No%20API%20key%20required-success)](#10-how-template-engine-mode-works)
[![Optional AI](https://img.shields.io/badge/Optional-LLM%20Enhanced%20Mode-8A2BE2)](#11-how-llm-enhanced-mode-works)

> **Clean the data before trusting the dashboard.**

A local-first and cloud-ready web application that helps anyone upload a CSV or Excel file and quickly understand whether the dataset is ready for analysis, dashboarding, reporting, or AI-assisted insights. It profiles the data, detects quality issues, produces a **Data Quality Score** and a **Dashboard Readiness Score**, provides a specialized **Retail Data Validation** suite, drafts an automated data dictionary, and generates executive-ready audit reports — all functional without requiring an API key or internet connection, with optional AI enhancement.

---

## 🚀 Live Demo

Try the live application in your browser:
👉 **[https://ai-data-readiness-auditor-g94hkbe2thkhwu9yrv3l5a.streamlit.app/](https://ai-data-readiness-auditor-g94hkbe2thkhwu9yrv3l5a.streamlit.app/)**

No installation or API key required. You can test immediately using the built-in sample datasets!

---

## Quick Start (Run Locally)

```bash
# 1. Clone the repository
git clone https://github.com/aditeeping13/ai-data-readiness-auditor.git
cd ai-data-readiness-auditor

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Launch the app
python -m streamlit run app.py
```

Then open `http://localhost:8501`, click **Load sample dataset**, and press **Run Data Readiness Audit**.

> **One-click launcher:** On Windows, double-click **`run_app.bat`**; on macOS/Linux, run **`./run_app.sh`** — both will automatically configure a virtual environment, install dependencies, and launch the application.

---

## 1. Project Overview

Teams constantly want dashboards, reports, and AI insights, but source data is frequently incomplete, duplicated, inconsistent, poorly structured, or not ready for trusted analysis.

The **AI Data Readiness Auditor** catches these issues before they corrupt downstream analytics. Upload a messy file or retail transactions, click **Run Audit**, and get a comprehensive readiness assessment, transparent scores, actionable recommendations, and domain-specific validation rules.

---

## 2. Core Problem Solved

- **Prevents flawed dashboards**: Decisions made on dirty data lead to costly mistakes.
- **Identifies hidden traps**: Uncovers unparseable dates, placeholder nulls (e.g., `"N/A"`, `"TBD"`), duplicate primary keys, and inconsistent text casing.
- **Saves analyst hours**: Replaces manual ad-hoc profiling scripts with an automated, reproducible audit.
- **Bridges business & technical communication**: Generates clear, component-level scorecards, automated data dictionaries, and executive summaries for non-technical stakeholders.
- **Guarantees retail transaction integrity**: Validates specialized retail rules (non-negative pricing, integer inventory, non-blank product IDs, transaction uniqueness).

---

## 3. Application Walkthrough & Tabs

The application features 8 dedicated tabs designed for a seamless end-to-end data audit workflow:

| Tab | Key Capabilities |
| --- | --- |
| **1. Upload & Preview** | Upload CSV or Excel (.xlsx) files; preview raw data, column types, and record counts; one-click loader for generic messy data or retail sample data. |
| **2. Audit Results** | Displays overall **Data Quality Score** and **Dashboard Readiness Score** (0–100); summary metrics; transparent penalty breakdowns across all quality dimensions. |
| **3. Data Quality Dashboard** | Interactive Plotly visualizers: score gauges, column health overview, missingness distribution, categorical cardinality, and numeric outlier visualizers. |
| **4. Retail Validation** | Domain-specific checks for retail & e-commerce datasets: verifies Product IDs, non-negative pricing, integer inventory quantities, and duplicate Transaction IDs with a downloadable error log. |
| **5. Recommendations** | Structured **Issue Log** (severity, recommended fix, business impact); automated **Data Dictionary** with inferred BI roles (Metric, Dimension, Date, ID, Text); **Dashboard Readiness Advisor**; and field-aware **Chart Gallery**. |
| **6. Cleaned Data** | Non-destructive, reversible cleaning toggles (strip whitespace, normalize blank-like strings, drop duplicates, title-case categories) with live before/after comparison and clean CSV export. |
| **7. Saved Audits** | Local SQLite-backed audit history: tracks quality score progression, per-audit comparisons, and issue count trends over time. |
| **8. Exports** | One-click downloads for comprehensive 20-section **Markdown reports**, cleaned dataset CSV, column profile CSV, and structured issue log CSV. |

---

## 4. Key Features in Detail

### 🔍 Comprehensive Profiling Engine
- **Column profiling**: Inferred types (numeric, datetime, categorical, boolean, text, identifier).
- **Missing-value detection**: Identifies true nulls plus 17+ placeholder variations (`"N/A"`, `"none"`, `"unknown"`, `"-"`, `"tbd"`, `"?"`).
- **Duplicate analysis**: Detects exact row duplicates and primary key collisions.
- **Category consistency**: Checks casing irregularities, leading/trailing whitespace, and high cardinality.
- **Date & temporal health**: Parse success rates, chronological consistency, future dates, and archaic dates.
- **Numeric & outlier analysis**: IQR-based outlier flagging, min/max/median/std metrics, and unexpected negative values.

### 🛍️ Retail Data Validation Suite
Specialized rule checks for e-commerce and retail transaction files:
- **Product ID Integrity**: Flags missing, blank, or placeholder identifiers.
- **Price Integrity**: Ensures prices are valid non-negative numbers.
- **Inventory Quantities**: Validates that stock quantities are non-negative whole integers.
- **Transaction Uniqueness**: Detects repeated transaction IDs after initial occurrence.
- **Downloadable Error Log**: Exports affected rows, rule violations, failed values, and clear remedial messages.

### 📊 Transparent Scoring Methodology
- **Data Quality Score (0–100)**: Component penalties for missing data, duplicates, invalid dates, outliers, and categorical inconsistencies.
- **Dashboard Readiness Score (0–100)**: Evaluates whether the dataset possesses necessary dimensions, metrics, time fields, and volume for reliable BI reporting.
- **Rating Tiers**: Ready ($\ge 85$), Minor Issues (70–84), Needs Cleanup (50–69), High Risk ($< 50$).

### 🔄 Dual-Engine Architecture
1. **Template Engine Mode (Default & 100% Offline)**:
   - Deterministic, zero-dependency, local template generator.
   - Requires no API keys, no internet connection, and zero external network calls.
2. **LLM Enhanced Mode (Optional AI Narratives)**:
   - Adds rich, context-aware AI narratives, business questions, and risk analysis.
   - Supports 6 LLM providers: **Groq**, **Google Gemini**, **OpenAI**, **Anthropic Claude**, **OpenRouter**, and **Azure OpenAI**.
   - Built exclusively with Python standard library (`urllib`) — zero extra pip packages needed.
   - Seamlessly loads API keys from local `.env` or cloud **Streamlit Secrets** (`st.secrets`).
   - Automatically and gracefully falls back to Template Engine Mode if no key is present or if network errors occur.

---

## 5. Technology Stack

- **Frontend & App Framework**: [Streamlit](https://streamlit.io/)
- **Data Processing & Profiling**: [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Excel Handling**: [openpyxl](https://openpyxl.readthedocs.io/)
- **Visualizations**: [Plotly Express](https://plotly.com/python/)
- **Database / Audit Persistence**: [SQLite3](https://docs.python.org/3/library/sqlite3.html) (Python standard library)
- **Deployment**: [Streamlit Community Cloud](https://streamlit.io/cloud)

---

## 6. Project Structure

```
ai-data-readiness-auditor/
├── app.py                     # Main Streamlit multi-tab application
├── requirements.txt           # Dependency specifications
├── README.md                  # Project documentation
├── LICENSE                    # MIT License
├── run_app.bat                # One-click Windows runner
├── run_app.sh                 # One-click Unix/macOS runner
├── .env.example               # Template for optional LLM configuration
├── .gitignore                 # Protects keys, temporary files, and local DBs
├── data/
│   └── data_readiness.db      # SQLite audit history (generated on first run)
├── outputs/                   # Destination for generated export files
├── sample_files/
│   ├── sample_messy_dataset.csv  # Generic messy test dataset
│   └── sample_retail_data.csv    # Specialized retail validation dataset
├── tests/
│   └── test_retail_validation.py # Unit tests for retail validation suite
└── src/
    ├── __init__.py
    ├── audit_engine.py        # Core profiling and audit logic
    ├── retail_validation.py   # Specialized retail rule validator
    ├── scoring.py             # Data quality & readiness scoring formulas
    ├── template_engine.py     # Deterministic offline narrative generation
    ├── db.py                  # SQLite persistence & trend tracking
    ├── exporters.py           # Markdown report and CSV builders
    ├── validators.py          # Input file validation & parsing
    ├── visualizations.py      # Plotly interactive score gauges and charts
    ├── sample_data.py         # Synthetic messy data generator
    ├── config.py              # App configuration, .env, and Streamlit secrets
    ├── utils.py               # Formatting, string, and file utilities
    └── providers/             # LLM provider abstraction layer
        ├── __init__.py
        ├── base_provider.py
        ├── template_provider.py
        └── llm_provider.py    # OpenAI-compatible, Azure, & Claude handlers
```

---

## 7. Configuration & AI Setup

### Local Configuration via `.env`
1. Make a copy of `.env.example` named `.env`:
   ```bash
   cp .env.example .env
   ```
2. Uncomment your chosen provider and add your API key:
   ```env
   LLM_PROVIDER=groq
   GROQ_API_KEY=gsk_your_groq_api_key_here
   ```
3. Start the app and select **LLM Enhanced Mode** in the sidebar.

### Streamlit Community Cloud Deployment Configuration
When deploying to Streamlit Community Cloud:
1. Open your app on Streamlit Cloud $\rightarrow$ Click **Settings** $\rightarrow$ **Secrets**.
2. Enter your secrets in TOML format:
   ```toml
   LLM_PROVIDER = "groq"
   GROQ_API_KEY = "gsk_your_groq_api_key_here"
   ```
3. The app automatically detects `st.secrets` and activates AI enhancement.

Supported Providers:
- **Groq** (`LLM_PROVIDER=groq`, `GROQ_API_KEY`)
- **Google Gemini** (`LLM_PROVIDER=gemini`, `GEMINI_API_KEY`)
- **OpenAI** (`LLM_PROVIDER=openai`, `OPENAI_API_KEY`)
- **Anthropic Claude** (`LLM_PROVIDER=claude`, `ANTHROPIC_API_KEY`)
- **OpenRouter** (`LLM_PROVIDER=openrouter`, `OPENROUTER_API_KEY`)
- **Azure OpenAI** (`LLM_PROVIDER=azure_openai`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`)

---

## 8. Running Automated Tests

Run the test suite using Python's built-in `unittest` runner:

```bash
python -m unittest discover -s tests -v
```

---

## 9. Example Use Cases

- **E-Commerce & Retail Operations**: Validate inventory spreadsheets, verify that all products have non-negative prices and positive stock counts, and deduplicate transaction IDs before ingest.
- **Business Intelligence & Analytics**: Audit CSV/Excel exports from CRM, ERP, or marketing platforms before building Power BI, Tableau, or Looker dashboards.
- **Data Engineering Pre-Checks**: Run quick schema, quality, and null checks on incoming vendor batches before writing ETL transformation pipelines.

---

## 10. Resume Highlights

- **Full-Stack Data Application**: Developed a cloud-deployed data profiling and readiness platform using Python, Streamlit, pandas, NumPy, SQLite, and Plotly Express.
- **Specialized Domain Validation**: Built an extensible retail rule engine to validate product IDs, pricing constraints, inventory quantities, and transaction uniqueness.
- **Hybrid Architecture**: Engineered a resilient dual-engine architecture offering 100% offline deterministic templates and optional LLM integration with automatic graceful fallback.
- **Stakeholder Deliverables**: Automated generation of 20-section executive Markdown audit summaries, data dictionaries, BI dashboard recommendations, and cleaned datasets.

---

## Open-Source Attribution

This project extends the MIT-licensed **AI Data Readiness Auditor** originally developed by **Gustavo Angulo**.

### Retail Validation Extension
- Added configurable validation rules for product identifiers, prices, inventory quantities, and transaction IDs.
- Added CSV-based issue reporting and automated validation tests.
- Deployed the extended application using Streamlit Community Cloud.

The original profiling, scoring, dashboard, and reporting functionality is based on the upstream project.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
