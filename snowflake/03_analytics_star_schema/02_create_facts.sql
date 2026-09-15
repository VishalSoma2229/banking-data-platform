-- ============================================================================
-- Script: 02_create_facts.sql
-- Purpose: Populate Fact Tables in ANALYTICS Schema
-- ============================================================================

USE ROLE ACCOUNTADMIN;
USE DATABASE BANKING_DB;
USE SCHEMA ANALYTICS;
USE WAREHOUSE COMPUTE_WH;

-- FCT_TRANSACTIONS
CREATE OR REPLACE TABLE FCT_TRANSACTIONS AS
SELECT 
    t.transaction_id,
    t.account_number,
    a.customer_id,
    a.branch_id,
    t.transaction_date,
    TO_DATE(t.transaction_date) AS transaction_date_key,
    t.transaction_type,
    t.channel,
    t.status AS transaction_status,
    t.amount,
    t.balance_after_txn,
    t.ingestion_timestamp AS loaded_at
FROM BANKING_DB.PUBLIC.TRANSACTION_MASTER t
LEFT JOIN BANKING_DB.PUBLIC.ACCOUNT_MASTER a ON t.account_number = a.account_number;

-- FCT_LOANS
CREATE OR REPLACE TABLE FCT_LOANS AS
SELECT 
    loan_id,
    customer_id,
    loan_type,
    start_date,
    tenure_months,
    loan_status,
    sanctioned_amount,
    outstanding_balance,
    interest_rate,
    (sanctioned_amount - outstanding_balance) AS total_amount_paid,
    ingestion_timestamp AS loaded_at
FROM BANKING_DB.PUBLIC.LOAN_MASTER;

-- FCT_FIXED_DEPOSITS
CREATE OR REPLACE TABLE FCT_FIXED_DEPOSITS AS
SELECT 
    fd_account_number,
    customer_id,
    start_date,
    maturity_date,
    tenure_months,
    fd_status,
    deposit_amount,
    interest_rate,
    maturity_amount,
    (maturity_amount - deposit_amount) AS total_expected_interest,
    ingestion_timestamp AS loaded_at
FROM BANKING_DB.PUBLIC.FD_MASTER;