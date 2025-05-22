import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("MYSQL_HOST").strip()
port = int(os.getenv("MYSQL_PORT").strip())
user = os.getenv("MYSQL_USER").strip()
password = os.getenv("MYSQL_PASSWORD").strip()
database = os.getenv("MYSQL_DB").strip()

def get_connection():
    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5
    )
