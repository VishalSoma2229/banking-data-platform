-- ============================================================================
-- Script: 03_kpi_queries.sql
-- Purpose: Executive Business Analytics & Materialized Aggregation Views
-- ============================================================================

USE ROLE ACCOUNTADMIN;
USE DATABASE BANKING_DB;
USE SCHEMA ANALYTICS;

-- 1. Executive Query: Overall Customer Exposure by Risk Category
SELECT 
    c.risk_category,
    COUNT(DISTINCT c.customer_id) AS total_customers,
    COALESCE(SUM(l.outstanding_balance), 0) AS total_loan_exposure,
    COALESCE(SUM(f.deposit_amount), 0) AS total_fixed_deposits
FROM BANKING_DB.ANALYTICS.DIM_CUSTOMER c
LEFT JOIN BANKING_DB.ANALYTICS.FCT_LOAN_SNAPSHOT l ON c.customer_id = l.customer_id
LEFT JOIN BANKING_DB.ANALYTICS.FCT_FD_SNAPSHOT f ON c.customer_id = f.customer_id
GROUP BY c.risk_category
ORDER BY total_loan_exposure DESC;

-- 2. Performance Materialized View: Branch Financial Metrics
CREATE OR REPLACE VIEW ANALYTICS.VW_BRANCH_FINANCIAL_SUMMARY AS
SELECT 
    b.branch_id,
    b.branch_name,
    b.city,
    COUNT(DISTINCT c.customer_id) AS customer_count,
    COALESCE(SUM(tnx.amount), 0) AS total_transaction_volume
FROM BANKING_DB.ANALYTICS.DIM_BRANCH b
INNER JOIN BANKING_DB.ANALYTICS.DIM_ACCOUNT acc ON acc.branch_id = b.branch_id
LEFT JOIN BANKING_DB.ANALYTICS.DIM_CUSTOMER c ON acc.customer_id = c.customer_id
LEFT JOIN BANKING_DB.ANALYTICS.FCT_TRANSACTIONS tnx ON c.customer_id = tnx.customer_id
GROUP BY b.branch_id, b.branch_name, b.city;