# Acquiring-processing-Bank-Information-IBM
Automated Python ETL pipeline extracting global banks market cap data, converting multi-currency rates (GBP/EUR/INR), logging progress, and persisting into CSV and SQLite.

# Automated ETL Pipeline: Global Banks Market Capitalization

An automated Python ETL (Extract, Transform, Load) pipeline designed to extract, transform, audit, and persist financial data on the world's top 10 largest banks by market capitalization.

---
## Architecture Overview

```mermaid
flowchart TD
    A[Wikipedia Archive HTML] -->|HTTP GET / BeautifulSoup| B[Raw Data Extraction]
    B -->|Pandas Transformation + exchange_rate.csv| C[Enriched Multi-Currency DataFrame]
    
    C -->|load_to_csv| D[(Largest_banks_data.csv)]
    C -->|load_to_db| E[(SQLite Database: Banks.db)]
    
    E -->|Automated Verification| F[SQL Query Execution]
    
    B -.->|Timestamps| G[code_log.txt]
    C -.->|Timestamps| G
    D -.->|Timestamps| G
    E -.->|Timestamps| G
    F -.->|Timestamps| G

---

## Tech Stack

* **Language:** Python 3.x
* **Web Scraping:** `requests`, `BeautifulSoup` (bs4)
* **Data Processing & Transformation:** `pandas`, `numpy`
* **Relational Storage:** `sqlite3`
* **Audit & Logging:** Python Standard Library (`datetime`)
