-- ============================================================================
-- Script: 01_database_and_schemas.sql
-- Purpose: Configure Compute Warehouse, Database, and Multi-Tier Schemas
-- ============================================================================

USE ROLE ACCOUNTADMIN;

-- 1. Create and Configure Compute Warehouse (Auto-Suspend enabled for trial efficiency)
CREATE WAREHOUSE IF NOT EXISTS COMPUTE_WH 
    WITH WAREHOUSE_SIZE = 'XSMALL' 
    AUTO_SUSPEND = 60 
    AUTO_RESUME = TRUE 
    INITIALLY_SUSPENDED = TRUE;

USE WAREHOUSE COMPUTE_WH;

-- 2. Database & Schema Initialization
CREATE DATABASE IF NOT EXISTS BANKING_DB;
USE DATABASE BANKING_DB;

-- Staging / Raw Layer
CREATE SCHEMA IF NOT EXISTS PUBLIC;

-- Business Analytics / Gold Layer
CREATE SCHEMA IF NOT EXISTS ANALYTICS;