# app/db/connection.py

import mysql.connector
from app.config import DB_CONFIG

def get_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn
