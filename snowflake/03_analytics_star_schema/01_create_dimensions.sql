-- ============================================================================
-- Script: 01_create_dimensions.sql
-- Purpose: Populate Dimension Tables in ANALYTICS Schema
-- ============================================================================

USE ROLE ACCOUNTADMIN;
USE DATABASE BANKING_DB;
USE SCHEMA ANALYTICS;
USE WAREHOUSE COMPUTE_WH;

-- DIM_CUSTOMER
CREATE OR REPLACE TABLE DIM_CUSTOMER AS
SELECT 
    customer_id,
    first_name,
    last_name,
    first_name || ' ' || last_name AS full_name,
    gender,
    date_of_birth,
    DATEDIFF('year', date_of_birth, CURRENT_DATE()) AS age,
    email,
    phone,
    pan_number,
    aadhaar_number,
    occupation,
    annual_income,
    marital_status,
    customer_since,
    kyc_status,
    risk_category,
    branch_id,
    city,
    state,
    country,
    customer_status,
    ingestion_timestamp AS created_at
FROM BANKING_DB.PUBLIC.CUSTOMER_MASTER;

-- DIM_BRANCH
CREATE OR REPLACE TABLE DIM_BRANCH AS
SELECT 
    branch_id,
    branch_name,
    city,
    state,
    ifsc_code,
    ingestion_timestamp AS created_at
FROM BANKING_DB.PUBLIC.BRANCH_MASTER;

-- DIM_ACCOUNT
CREATE OR REPLACE TABLE DIM_ACCOUNT AS
SELECT 
    account_number,
    customer_id,
    branch_id,
    account_type,
    currency,
    account_status,
    opened_date,
    ingestion_timestamp AS created_at
FROM BANKING_DB.PUBLIC.ACCOUNT_MASTER;

-- DIM_CARD
CREATE OR REPLACE TABLE DIM_CARD AS
SELECT 
    card_number,
    account_number,
    customer_id,
    card_type,
    card_category,
    expiry_date,
    card_status,
    ingestion_timestamp AS created_at
FROM BANKING_DB.PUBLIC.CARD_MASTER;