import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    st.error("API key not found. Please set the GOOGLE_API_KEY environment variable.")

def main():
    st.set_page_config(page_title="Simple QA with Documents")
    st.header("Ask a Question About Your Document")

    uploaded_file = st.file_uploader("Upload your document", type=["txt", "md", "pdf"])
    user_question = st.text_input("Your Question")

    if st.button("Submit") and uploaded_file is not None and user_question:
        try:
            # Read file content
            file_content = uploaded_file.read().decode("utf-8", errors="ignore")

            # Combine file content and question as prompt
            prompt = f"""You are a helpful assistant. Based on the following document, answer the user's question.

Document:
{file_content}

Question: {user_question}
Answer:"""

            # Use Gemini model
            model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
            response = model.generate_content(prompt)

            # Show the answer
            st.subheader("Answer:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
