from app.db.schema_reader import get_table_schema
from app.db.connection import get_connection
from app.llm.agent import query_ollama

def clean_sql_response(response: str) -> str:
    if "```" in response:
        response = response.replace("```sql", "").replace("```", "").strip()
    if "SELECT" in response.upper():
        response = response[response.upper().find("SELECT"):]
    return response.strip()

def run_user_query(user_input: str):
    # Step 1: Fetch Schema
    schema_dict = get_table_schema()
    schema_text = ""
    for table, cols in schema_dict.items():
        col_names = ", ".join([col[0] for col in cols])
        schema_text += f"Table: {table}\nColumns: {col_names}\n\n"

    # Step 2: Prompt Construction
    prompt = f"""
You are a highly accurate SQL assistant.

Use the following MySQL schema:

{schema_text}

The user will ask a question in natural language. Convert it into a syntactically correct SQL query.

⚠️ Important:
- Use the correct columns from the correct tables.
- Do NOT guess columns.
- Only respond with the SQL query. No formatting or explanations.

Question: {user_input}
SQL:
"""


    # Step 3: Get SQL from LLM
    raw_response = query_ollama(prompt)
    sql_query = clean_sql_response(raw_response)

    print("\n📄 Generated SQL:\n", sql_query)

    # Step 4: Execute SQL
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        return {"error": str(e)}
