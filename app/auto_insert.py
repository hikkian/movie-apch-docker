import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import random
import time
from datetime import datetime
from sqlalchemy import create_engine, text
from app.config import DB_URL

engine = create_engine(DB_URL)

def insert_new_rating():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COALESCE(MAX(rating_id), 0) FROM ratings"))
        max_id = result.scalar()
        new_id = max_id + 1

        user_id = random.randint(1, 5000)
        movie_id = random.randint(1, 20000)
        rating = round(random.uniform(1.0, 10.0), 1)

        conn.execute(
            text("""
                INSERT INTO ratings (rating_id, user_id, movie_id, rating)
                VALUES (:rating_id, :user_id, :movie_id, :rating)
            """),
            {
                "rating_id": new_id,
                "user_id": user_id,
                "movie_id": movie_id,
                "rating": rating
            } 
        )

        conn.commit()
        print(f"✅ Inserted rating {new_id}")

if __name__ == "__main__":
    print("🔄 Auto-insert started. Press Ctrl+C to stop.")
    while True:
        insert_new_rating()
        time.sleep(5)
