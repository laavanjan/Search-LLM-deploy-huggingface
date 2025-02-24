import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env (if running locally)
load_dotenv()

# Debug: Print environment variables
st.write("🔍 Debugging Environment Variables")
st.write("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))
st.write("LANGCHAIN_API_KEY:", os.getenv("LANGCHAIN_API_KEY"))

# Ensure API keys exist before proceeding
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not LANGCHAIN_API_KEY or not GROQ_API_KEY:
    st.error("❌ API keys are missing. Please check GitHub Secrets or .env file.")
    st.stop()

# Now set environment variables
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
