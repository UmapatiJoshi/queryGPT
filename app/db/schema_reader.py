# app/db/schema_reader.py

from app.db.connection import get_connection

def get_table_schema():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor.fetchall()]
    
    schema = {}
    for table in tables:
        cursor.execute(f"DESCRIBE {table}")
        schema[table] = cursor.fetchall()

    cursor.close()
    conn.close()
    return schema
