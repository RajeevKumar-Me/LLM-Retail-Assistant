import streamlit as st
from main import main

st.set_page_config(
    page_title="Retail AI Assistant",
    page_icon="🛍️",
    layout="centered"
)

st.title("🛍️ Retail AI Assistant")
st.write(
    "Ask questions about inventory, products, recommendations, and retail insights."
)

question = st.text_input(
    "Enter your question:"
)

if st.button("Generate Answer"):
    if question:
        with st.spinner("Thinking..."):
            answer = main(question)
        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")