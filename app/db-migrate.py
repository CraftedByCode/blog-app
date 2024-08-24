import pandas as pd
from sqlalchemy import create_engine, inspect

# SQLite connection
sqlite_engine = create_engine("sqlite:///./blog.db")

# PostgreSQL connection
postgres_engine = create_engine(
    "postgresql://default:msq78RwNxTIE@ep-curly-king-a1cx2zm9-pooler.ap-southeast-1.aws.neon.tech:5432/verceldb"
)

# Use the inspect module to get table names
inspector = inspect(sqlite_engine)
tables = inspector.get_table_names()

# Loop through the tables and migrate each one
for table in tables:
    # Read table from SQLite
    df = pd.read_sql_table(table, sqlite_engine)

    # Write table to PostgreSQL
    df.to_sql(table, postgres_engine, if_exists="replace", index=False)
