import pandas as pd
from sqlalchemy import create_engine
from transform_data import transform_data, extract_data

# Database connection details
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
USER = 'alekhya'  # Change this
PASSWORD = 'alekhya'  # Change this
HOST = 'localhost'
PORT = '5432'
DATABASE = 'etl_project'

# Create the database engine
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

# Load step: Save transformed data to PostgreSQL
def load_data(df):
    df.to_sql("movies", engine, if_exists="replace", index=False)
    print("✅ Data successfully loaded into PostgreSQL!")

if __name__ == "__main__":
    df_transformed = transform_data(extract_data())  # Run extract & transform steps
    load_data(df_transformed)
