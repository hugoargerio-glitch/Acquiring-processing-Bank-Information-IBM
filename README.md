# Acquiring-processing-Bank-Information-IBM
Automated Python ETL pipeline extracting global banks market cap data, converting multi-currency rates (GBP/EUR/INR), logging progress, and persisting into CSV and SQLite.

# Automated ETL Pipeline: Global Banks Market Capitalization

An automated Python ETL (Extract, Transform, Load) pipeline designed to extract, transform, audit, and persist financial data on the world's top 10 largest banks by market capitalization.

---

## Architecture & Data Flow

1. **Source Layer:** Target table from archived Wikipedia web page.
2. **Extraction Engine:** Automated scraping and parsing via `requests` and `BeautifulSoup4`.
3. **Transformation Layer:** 
   * Ingestion of `exchange_rate.csv`.
   * Currency calculations for GBP, EUR, and INR using Pandas/NumPy vectorization.
4. **Persistence Layer:**
   * **Flat-File:** Exported to `Largest_banks_data.csv`.
   * **RDBMS:** Inserted into table `Largest_banks` in `Banks.db` (SQLite).
5. **Validation & Auditing:** Automated SQL queries execution and centralized timestamp logging in `code_log.txt`.

---

## Tech Stack

* **Language:** Python 3.x
* **Web Scraping:** `requests`, `BeautifulSoup` (bs4)
* **Data Processing & Transformation:** `pandas`, `numpy`
* **Relational Storage:** `sqlite3`
* **Audit & Logging:** Python Standard Library (`datetime`)
