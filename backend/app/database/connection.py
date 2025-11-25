import sqlite3
from app.config.settings import DB_PATH
import os

# Crea DATA_DIR si no existe
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn
