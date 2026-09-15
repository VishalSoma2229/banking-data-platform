-- ============================================================================
-- Script: 01_create_raw_tables.sql
-- Purpose: DDL Scripts for 7 Staging/Raw Master Tables (PUBLIC Schema)
-- ============================================================================

USE ROLE ACCOUNTADMIN;
USE DATABASE BANKING_DB;
USE SCHEMA PUBLIC;

CREATE OR REPLACE TABLE CUSTOMER_MASTER (
    customer_id         VARCHAR(50),
    first_name          VARCHAR(100),
    last_name           VARCHAR(100),
    gender              VARCHAR(10),
    date_of_birth       DATE,
    email               VARCHAR(150),
    phone               VARCHAR(20),
    pan_number          VARCHAR(20),
    aadhaar_number      VARCHAR(20),
    occupation          VARCHAR(100),
    annual_income       NUMBER(15,2),
    marital_status      VARCHAR(20),
    customer_since      DATE,
    kyc_status          VARCHAR(20),
    risk_category       VARCHAR(20),
    branch_id           VARCHAR(20),
    city                VARCHAR(100),
    state               VARCHAR(100),
    country             VARCHAR(100),
    customer_status     VARCHAR(20),
    ingestion_timestamp TIMESTAMP_NTZ
);

CREATE OR REPLACE TABLE ACCOUNT_MASTER (
    account_number      VARCHAR(50),
    customer_id         VARCHAR(50),
    account_type        VARCHAR(30),
    balance             NUMBER(15,2),
    currency            VARCHAR(10),
    account_status      VARCHAR(20),
    opened_date         DATE,
    branch_id           VARCHAR(20),
    ingestion_timestamp TIMESTAMP_NTZ
);

CREATE OR REPLACE TABLE BRANCH_MASTER (
    branch_id           VARCHAR(20),
    branch_name         VARCHAR(100),
    city                VARCHAR(100),
    state               VARCHAR(100),
    ifsc_code           VARCHAR(20),
    ingestion_timestamp TIMESTAMP_NTZ
);

CREATE OR REPLACE TABLE CARD_MASTER (
    card_number         VARCHAR(50),
    account_number      VARCHAR(50),
    customer_id         VARCHAR(50),
    card_type           VARCHAR(30),
    card_category       VARCHAR(30),
    expiry_date         DATE,
    credit_limit        NUMBER(15,2),
    available_credit    NUMBER(15,2),
    card_status         VARCHAR(20),
    ingestion_timestamp TIMESTAMP_NTZ
);

CREATE OR REPLACE TABLE FD_MASTER (
    fd_account_number   VARCHAR(50),
    customer_id         VARCHAR(50),
    deposit_amount      NUMBER(15,2),
    interest_rate       NUMBER(5,2),
    tenure_months       INT,
    start_date          DATE,
    maturity_date       DATE,
    maturity_amount     NUMBER(15,2),
    fd_status           VARCHAR(20),
    ingestion_timestamp TIMESTAMP_NTZ
);

CREATE OR REPLACE TABLE LOAN_MASTER (
    loan_id             VARCHAR(50),
    customer_id         VARCHAR(50),
    loan_type           VARCHAR(30),
    sanctioned_amount   NUMBER(15,2),
    outstanding_balance NUMBER(15,2),
    interest_rate       NUMBER(5,2),
    tenure_months       INT,
    start_date          DATE,
    loan_status         VARCHAR(20),
    ingestion_timestamp TIMESTAMP_NTZ
);

CREATE OR REPLACE TABLE TRANSACTION_MASTER (
    transaction_id      VARCHAR(50),
    account_number      VARCHAR(50),
    transaction_date    TIMESTAMP_NTZ,
    transaction_type    VARCHAR(20),
    amount              NUMBER(15,2),
    balance_after_txn   NUMBER(15,2),
    channel             VARCHAR(30),
    status              VARCHAR(20),
    ingestion_timestamp TIMESTAMP_NTZ
);