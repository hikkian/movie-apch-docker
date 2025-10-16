import pandas as pd
from config import engine

def load_data():
    tables = ["genres", "directors", "actors", "users", "movies", "movie_actor", "ratings"]
    
    for table in tables:
        try:
            df = pd.read_csv(f"/datasets/{table}.csv")
            df.to_sql(table, engine, if_exists="append", index=False)
            print(f"✅ Loaded {len(df)} rows into {table}")
        except Exception as e:
            print(f"⚠️ Error loading {table}: {e}")

if __name__ == "__main__":
    load_data()
