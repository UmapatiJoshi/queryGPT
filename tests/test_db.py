# tests/test_schema_reader.py

from app.db.schema_reader import get_table_schema

def test_schema():
    schema = get_table_schema()
    print("📊 Extracted Schema:\n")
    for table, fields in schema.items():
        col_names = [col[0] for col in fields]
        print(f"- {table}: {col_names}")

if __name__ == "__main__":
    test_schema()
