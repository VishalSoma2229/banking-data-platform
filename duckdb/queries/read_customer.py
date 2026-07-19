import duckdb


def read_customer_data():
    con = duckdb.connect()

    try:
        # Load HTTPFS extension
        con.execute("INSTALL httpfs;")
        con.execute("LOAD httpfs;")

        # Configure MinIO
        con.execute("SET s3_endpoint='localhost:8050';")
        con.execute("SET s3_access_key_id='azure_admin';")
        con.execute("SET s3_secret_access_key='azure_password';")
        con.execute("SET s3_use_ssl=false;")
        con.execute("SET s3_url_style='path';")

        query = """
        SELECT
        country,
        COUNT(*) AS total_customers
        FROM read_parquet('s3://banking-lake/gold/customer/*.parquet')
        GROUP BY country;
        """

        df = con.execute(query).fetchdf()

        print("\nCustomer Gold Data")
        print("=" * 80)
        print(df)

    finally:
        con.close()


if __name__ == "__main__":
    read_customer_data()