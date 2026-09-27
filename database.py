import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def connect_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        return conn

    except psycopg2.Error as e:
        print("Database connection failed:", e)
        return None