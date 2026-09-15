-- ============================================================================
-- Script: 01_streams_and_tasks.sql
-- Purpose: Change Data Capture (CDC) via Streams and Automated Task Refresh
-- ============================================================================

USE ROLE ACCOUNTADMIN;
USE DATABASE BANKING_DB;
USE WAREHOUSE COMPUTE_WH;

-- 1. Capture CDC on Raw Transaction Master
CREATE OR REPLACE STREAM PUBLIC.TRANSACTION_STREAM 
ON TABLE PUBLIC.TRANSACTION_MASTER;

-- 2. Automated Task to Process Incremental Inserts
CREATE OR REPLACE TASK ANALYTICS.TASK_REFRESH_FCT_TRANSACTIONS
    WAREHOUSE = COMPUTE_WH
    SCHEDULE = '5 MINUTE'
WHEN
    SYSTEM$STREAM_HAS_DATA('PUBLIC.TRANSACTION_STREAM')
AS
INSERT INTO BANKING_DB.ANALYTICS.FCT_TRANSACTIONS
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
FROM PUBLIC.TRANSACTION_STREAM t
LEFT JOIN PUBLIC.ACCOUNT_MASTER a ON t.account_number = a.account_number
WHERE METADATA$ACTION = 'INSERT';

-- Note: Resume task when executing live stream tests
-- ALTER TASK ANALYTICS.TASK_REFRESH_FCT_TRANSACTIONS RESUME;