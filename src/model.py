import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def load_model():
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("google_api_key")
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
    return ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0.3,
        max_output_tokens=500,
        thinking_budget=0,
    )
 
