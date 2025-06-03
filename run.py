from app.main import run_user_query

if __name__ == "__main__":
    question = input("💬 Ask your question: ")
    result = run_user_query(question)

    if isinstance(result, list):
        print("\n📊 Results:")
        for row in result:
            print(row)
    else:
        print("\n❌ Error:", result.get("error"))
