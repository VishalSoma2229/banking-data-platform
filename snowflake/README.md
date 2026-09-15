# Enterprise Banking Data Warehouse & Pipeline Platform

An end-to-end cloud data engineering platform designed to ingest, clean, model, and secure core banking domain datasets using **PySpark** and **Snowflake Data Warehouse**.

---

## 🛠 Tech Stack
* **Processing & ETL:** PySpark
* **Data Storage:** Apache Parquet
* **Data Warehouse:** Snowflake (SnowSQL)
* **Modeling:** Star Schema Dimensional Modeling (Facts & Dimensions)
* **Automation & Security:** Snowflake Streams, Tasks, Dynamic Data Masking, RBAC

---

## 🏛 Architecture Overview
1. **Raw CSV Source Processing:** Extracted raw banking data across 7 domain datasets (Customers, Accounts, Transactions, Cards, Loans, Fixed Deposits, Branches). Applied PySpark transformations for case normalization, whitespace trimming, and schema standardization.
2. **Optimized Parquet Storage:** Exported coalesced Parquet files to local storage to prevent small-file overhead.
3. **Snowflake Ingestion:** Uploaded files to `@BANKING_STAGE` and executed schema-matched bulk loads using `COPY INTO` with auto-matching parameters.
4. **Analytics Layer (Star Schema):** Modeled data into dimensional entities (`DIM_CUSTOMER`, `DIM_BRANCH`, `DIM_ACCOUNT`, `DIM_CARD`) and transactional facts (`FCT_TRANSACTIONS`, `FCT_LOANS`, `FCT_FIXED_DEPOSITS`).
5. **Governance & Automation:** Built Change Data Capture (CDC) via Snowflake **Streams** & **Tasks**, alongside column-level **Dynamic Data Masking** for sensitive PII data (Aadhaar & PAN).

---

## 📂 Project Structure
```text
banking_snowflake_project/
│
├── 01_setup/
│   ├── 01_database_and_schemas.sql    -- Database, Warehouses, and Schemas
│   └── 02_stages_and_formats.sql     -- Stage & Parquet File Formats
│
├── 02_raw_ingestion/
│   ├── 01_create_raw_tables.sql      -- Staging Table DDLs
│   └── 02_copy_into_raw.sql          -- Bulk COPY INTO execution
│
├── 03_analytics_star_schema/
│   ├── 01_create_dimensions.sql      -- DIM_ Table Transformations
│   └── 02_create_facts.sql           -- FCT_ Table Transformations
│
├── 04_advanced_features/
│   ├── 01_streams_and_tasks.sql      -- CDC Stream Automation
│   ├── 02_security_masking.sql       -- PII Data Masking & RBAC
│   └── 03_kpi_queries.sql            -- Analytical Views & Reporting Queries
│
└── README.md                         -- Project Documentation