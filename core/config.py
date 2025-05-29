import os

from dotenv import load_dotenv

load_dotenv(
    dotenv_path=".env"
)

DB_NAME=os.getenv("DB_NAME")
DB_PORT=os.getenv("DB_PORT")
DB_HOST=os.getenv("DB_HOST")
DB_USER=os.getenv("DB_USER")
DB_PASS=os.getenv("DB_PASS")


DB_CONFIG = {
    "database": DB_NAME,
    "port": DB_PORT,
    "host": DB_HOST,
    "user": DB_USER,
    "password": DB_PASS
}