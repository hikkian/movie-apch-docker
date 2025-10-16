from sqlalchemy import create_engine, text

engine = create_engine("sqlite:////app/sqlite_data/movies.db", future=True)

def create_tables():
    with engine.connect() as conn:
        # Enable foreign keys in SQLite
        conn.execute(text("PRAGMA foreign_keys = ON;"))
        
        # Remove CASCADE and execute statements separately
        conn.execute(text("DROP TABLE IF EXISTS ratings"))
        conn.execute(text("DROP TABLE IF EXISTS movie_actor"))
        conn.execute(text("DROP TABLE IF EXISTS users"))
        conn.execute(text("DROP TABLE IF EXISTS movies"))
        conn.execute(text("DROP TABLE IF EXISTS directors"))
        conn.execute(text("DROP TABLE IF EXISTS actors"))
        conn.execute(text("DROP TABLE IF EXISTS genres"))

        conn.execute(text("""
            CREATE TABLE genres (
                genre_id INT PRIMARY KEY,
                name TEXT
            )
        """))

        conn.execute(text("""
            CREATE TABLE directors (
                director_id INT PRIMARY KEY,
                name TEXT
            )
        """))

        conn.execute(text("""
            CREATE TABLE movies (
                movie_id INT PRIMARY KEY,
                title TEXT,
                release_year INT,
                genre_id INT REFERENCES genres(genre_id),
                director_id INT REFERENCES directors(director_id),
                duration_min INT,
                latitude DECIMAL(10, 6),
                longitude DECIMAL(10, 6),
                production_city VARCHAR(100)
            )
        """))

        conn.execute(text("""
            CREATE TABLE actors (
                actor_id INT PRIMARY KEY,
                name TEXT
            )
        """))

        conn.execute(text("""
            CREATE TABLE movie_actor (
                movie_id INT REFERENCES movies(movie_id),
                actor_id INT REFERENCES actors(actor_id),
                PRIMARY KEY (movie_id, actor_id)
            )
        """))

        conn.execute(text("""
            CREATE TABLE users (
                user_id INT PRIMARY KEY,
                username TEXT
            )
        """))

        conn.execute(text("""
            CREATE TABLE ratings (
                rating_id INT PRIMARY KEY,
                user_id INT REFERENCES users(user_id),
                movie_id INT REFERENCES movies(movie_id),
                rating NUMERIC,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))

        conn.commit()
        print("✅ Tables created successfully")

if __name__ == "__main__":
    create_tables()
