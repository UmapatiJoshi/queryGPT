
import streamlit as st
from app.main import run_user_query


st.set_page_config(page_title="QueryGPT", layout="wide")

st.title("🧠 QueryGPT - AI SQL Agent")
st.write("Ask a question in natural language, and I’ll query your database.")

# User Input
user_input = st.text_input("💬 Ask your query:")

# When submitted
if st.button("Run Query") and user_input:
    with st.spinner("Thinking..."):
        result = run_user_query(user_input)

    if isinstance(result, list):
        st.success("✅ Query executed successfully.")
        st.dataframe(result)
    else:
        st.error(f"❌ Error: {result.get('error')}")
        if "suggestion" in result:
            st.info("🤖 Suggested fix:")
            st.code(result["suggestion"], language="sql")
