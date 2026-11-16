import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def load_model():
    api_key = os.getenv("groq_api_key") or os.getenv("GROQ_API_KEY")
    if api_key:
        os.environ["GROQ_API_KEY"] = api_key
    return ChatGroq(model="openai/gpt-oss-120b", max_tokens=500, max_retries=1, request_timeout=20, reasoning_effort="low")
 
