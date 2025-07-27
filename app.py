import streamlit as st
from retriever import get_response

st.set_page_config(page_title="Movie Review RAG Chatbot")
st.title("Movie Review Q&A Chatbot")
st.markdown("Ask anything about movie reviews from IMDb dataset. Powered by Retrieval-Augmented Generation!")

query = st.text_input("Ask your question here:")

if query:
    with st.spinner("Generating intelligent answer..."):
        response = get_response(query)
        st.markdown("Chatbot Answer:")
        st.write(response)
