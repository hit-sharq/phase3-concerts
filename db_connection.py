import psycopg2
from psycopg2 import sql

def get_connection():
    """Create and return a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="joshualee087",
            host="localhost",     # e.g., "localhost"
            port="5432"      # e.g., "5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    