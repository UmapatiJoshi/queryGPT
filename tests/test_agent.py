from app.llm.agent import query_ollama

def clean_sql_response(response: str) -> str:
    # Strip markdown and unnecessary explanations
    if "```" in response:
        response = response.replace("```sql", "").replace("```", "").strip()
    # Optional: grab only the first SQL-looking line
    if "SELECT" in response.upper():
        response = response[response.upper().find("SELECT"):]
    return response.strip()

def test_model():
    schema = """
    Table: customers
    Columns: customer_id, name, email, created_at
    """

    user_question = "Show all customers."
    
    prompt = f"""
You are an expert SQL assistant.

Given the following schema:
{schema}

Respond ONLY with the correct SQL query.
No markdown, no code blocks, no explanations.

Question: {user_question}
SQL:
"""
    raw_response = query_ollama(prompt)
    cleaned_sql = clean_sql_response(raw_response)

    print("🧠 Raw Model Response:\n", raw_response)
    print("\n✅ Cleaned SQL:\n", cleaned_sql)

if __name__ == "__main__":
    test_model()
