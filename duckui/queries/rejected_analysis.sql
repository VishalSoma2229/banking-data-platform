SELECT *
FROM read_parquet(
    's3://banking-lake/rejected/account/*.parquet'
)
LIMIT 10;


SELECT *
FROM read_parquet(
    's3://banking-lake/rejected/branch/*.parquet'
)
LIMIT 10;


SELECT *
FROM read_parquet(
    's3://banking-lake/rejected/card/*.parquet'
)
LIMIT 10;


SELECT *
FROM read_parquet(
    's3://banking-lake/rejected/customer/*.parquet'
)
LIMIT 10;

SELECT *
FROM read_parquet(
    's3://banking-lake/rejected/fd/*.parquet'
)
LIMIT 10;


SELECT *
FROM read_parquet(
    's3://banking-lake/rejected/loan/*.parquet'
)
LIMIT 10;


SELECT *
FROM read_parquet(
    's3://banking-lake/rejected/transaction/*.parquet'
)
LIMIT 10;