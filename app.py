import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Keerthana Bellam | AI Portfolio", layout="wide")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Load profile data
with open("profile_data.txt", "r") as file:
    profile_info = file.read()

# ---- MAIN PORTFOLIO SECTION ----

col1, col2 = st.columns([1, 2])

with col1:
    st.image("profile.jpeg", width=250)
    st.markdown("### Keerthana Bellam")
    st.markdown("AI & Data Science Graduate Student")
    st.markdown("📍 New Jersey, USA")
    st.markdown("📧 keerthanabellam23@gmail.com")
    st.markdown("[LinkedIn](https://linkedin.com/in/YOUR-LINK)")

with col2:
    st.markdown("## About Me")
    st.write("""
    I am a Data Science graduate student transitioning into AI Engineering, 
    passionate about building intelligent systems using Machine Learning 
    and Generative AI technologies.
    """)

    st.markdown("## Key Projects")
    st.write("""
    - Heart Rate Estimation using Deep Learning  
    - Smart Farming Analytics (Random Forest + TensorFlow)  
    - Health Welfare Analysis (SVM + Sentiment Analysis)
    """)

# ---- FLOATING CHATBOT ----

st.markdown("---")
st.markdown("### 🤖 Ask My AI Assistant")

query = st.text_input("Ask about my experience, skills, or projects")

if query:
    prompt = f"""
    You are the AI assistant for Keerthana Bellam's portfolio.

    Only answer using the information below.
    If unknown, say:
    "I don't have that information yet.
    You can contact Keerthana at:
    Email: keerthanabellam23@gmail.com
    LinkedIn: https://linkedin.com/in/YOUR-LINK"

    Information:
    {profile_info}

    Question:
    {query}
    """

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        answer = response.choices[0].message.content

    st.success(answer)
