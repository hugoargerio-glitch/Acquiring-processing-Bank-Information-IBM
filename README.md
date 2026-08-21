# Global Banks Market Capitalization ETL Pipeline

An automated Python ETL (Extract, Transform, Load) pipeline designed to extract, transform, audit, and persist financial data on the world's top 10 largest banks by market capitalization.

---

## Architecture & Data Flow

* **Source Layer:** Target table from archived Wikipedia web page.
* **Extraction Engine:** Automated scraping and parsing via `requests` and `BeautifulSoup4`.
* **Transformation Layer:** 
  * Ingestion of `exchange_rate.csv`.
  * Currency calculations for GBP, EUR, and INR using Pandas/NumPy vectorization.
* **Persistence Layer:**
  * **Flat-File:** Exported to `Largest_banks_data.csv`.
  * **RDBMS:** Inserted into table `Largest_banks` in `Banks.db` (SQLite).
* **Validation & Auditing:** Automated SQL queries execution and centralized timestamp logging in `code_log.txt`.

---

## Tech Stack

* **Language:** Python 3.8+
* **Web Scraping:** `requests`, `beautifulsoup4`
* **Data Processing:** `pandas`, `numpy`
* **Storage:** `sqlite3` (Embedded RDBMS)
* **Auditing:** `datetime` (Python Standard Library)

---

## Repository Structure

```text
├── banks_project.py        # Main ETL script
├── exchange_rate.csv       # Conversion rates for GBP, EUR, INR
├── Largest_banks_data.csv  # Processed output dataset
├── Banks.db                # SQLite database
├── code_log.txt            # Audit trail log
├── .gitignore              # Ignored files
└── README.md               # Documentation
```

# Quickstart
##Clone the repository
git clone [https://github.com/hugoargerio-glitch/Acquiring-processing-Bank-Information-IBM.git](https://github.com/hugoargerio-glitch/Acquiring-processing-Bank-Information-IBM.git)
cd Acquiring-processing-Bank-Information-IBM

## Install dependencies
pip install requests beautifulsoup4 pandas numpy

## Run the pipeline
python banks_project.py
