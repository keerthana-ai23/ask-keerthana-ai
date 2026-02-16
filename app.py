import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Ask Keerthana AI", page_icon="🤖")

st.title("Ask Keerthana AI 🤖")
st.write("Ask about my experience, skills, or projects!")

# Load API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Load profile data
with open("profile_data.txt", "r") as file:
    profile_info = file.read()

# Chat input
query = st.chat_input("Ask a question about Keerthana...")

if query:
    prompt = f"""
    You are an AI assistant representing Keerthana Bellam.

    Answer professionally and clearly using ONLY the information below.
    If the answer is not in the information, say you don't have that information.

    Information:
    {profile_info}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)
