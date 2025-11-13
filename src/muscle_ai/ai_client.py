import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel("gemini-2.5-pro")


def ask_gemini(question: str) -> str:
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e: 
        print(f"Error during AI request: {e}")
        return None
