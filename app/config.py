from sqlalchemy import create_engine

DB_FILE = "/app/sqlite_data/movies.db"
DB_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(DB_URL, future=True)
