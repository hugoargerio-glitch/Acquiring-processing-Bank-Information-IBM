# Acquiring-processing-Bank-Information-IBM
Automated Python ETL pipeline extracting global banks market cap data, converting multi-currency rates (GBP/EUR/INR), logging progress, and persisting into CSV and SQLite.

# Automated ETL Pipeline: Global Banks Market Capitalization

An automated Python ETL (Extract, Transform, Load) pipeline designed to extract, transform, audit, and persist financial data on the world's top 10 largest banks by market capitalization.

---

## Architecture & Data Flow

[ Wikipedia Web Archive ]
│
▼ (Web Scraping - BeautifulSoup)
[ Raw Data ]
│
▼ (Currency Conversion - Pandas & NumPy)
[ Transformed Data ]
│            │
▼            ▼
[ CSV File ]  [ SQLite DB ] ──► (Automated SQL Queries)
│            │
└─────┬──────┘
▼
[ code_log.txt ] (Execution Audit Trail)


---

## Tech Stack

* **Language:** Python 3.x
* **Web Scraping:** `requests`, `BeautifulSoup` (bs4)
* **Data Processing & Transformation:** `pandas`, `numpy`
* **Relational Storage:** `sqlite3`
* **Audit & Logging:** Python Standard Library (`datetime`)
