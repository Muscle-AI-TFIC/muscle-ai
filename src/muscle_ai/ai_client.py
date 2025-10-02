import os
import google.generativeai as genai
from dotenv import load_dotenv

#calling .env
load_dotenv()

#configuring the api key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#selecting the type of model
model = genai.GenerativeModel("gemini-2.5-pro")


#sending a question to gemini and showing the response
def ask_gemini(question: str) -> str:
    response = model.generate_content(question)
    return response.text
