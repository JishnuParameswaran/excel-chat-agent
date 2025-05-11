import streamlit as st
from agent.agent import DataAnalysisAgent

def main():
    st.title("📊 Excel/CSV Chat Agent")
    uploaded_file = st.file_uploader("Upload your file", type=["csv", "xlsx"])
    if uploaded_file:
        agent = DataAnalysisAgent(uploaded_file)
        user_query = st.text_input("Ask a question about your data:")
        if user_query:
            response = agent.run(user_query)
            st.write(response)

if __name__ == "__main__":
    main()