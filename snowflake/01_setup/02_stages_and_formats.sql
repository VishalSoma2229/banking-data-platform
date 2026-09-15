-- ============================================================================
-- Script: 02_stages_and_formats.sql
-- Purpose: Define Parquet File Format and Internal Staging Area
-- ============================================================================

USE ROLE ACCOUNTADMIN;
USE DATABASE BANKING_DB;
USE SCHEMA PUBLIC;

-- 1. Create Parquet File Format
CREATE OR REPLACE FILE FORMAT PUBLIC.PARQUET_FORMAT 
    TYPE = 'PARQUET'
    COMPRESSION = 'SNAPPY';

-- 2. Create Named Internal Stage for Data Loading
CREATE OR REPLACE STAGE PUBLIC.BANKING_STAGE
    FILE_FORMAT = PUBLIC.PARQUET_FORMAT;