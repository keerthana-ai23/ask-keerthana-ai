import streamlit as st
from openai import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Streamlit page config
st.set_page_config(page_title="Ask Keerthana AI", page_icon="🤖")

st.title("Ask Keerthana AI 🤖")
st.write("Ask me about my experience, projects, or skills!")

# Load OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Load profile data
loader = TextLoader("profile_data.txt")
documents = loader.load()

# Split text into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OpenAIEmbeddings(api_key=st.secrets["OPENAI_API_KEY"])
vectorstore = FAISS.from_documents(docs, embeddings)

# Chat input
query = st.chat_input("Ask a question about Keerthana...")

if query:
    results = vectorstore.similarity_search(query, k=3)
    context = "\n".join([doc.page_content for doc in results])

    prompt = f"""
    You are an AI assistant representing Keerthana Bellam.
    Answer professionally and clearly using ONLY the information provided below.

    Information:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)
