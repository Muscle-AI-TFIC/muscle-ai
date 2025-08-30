import os
import google.generativeai as genai
from dotenv import load_dotenv

#puxando .env
load_dotenv()

#configurando a chave da api
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#selecionando o modelo do gemini
model = genai.GenerativeModel("gemini-2.5-pro")


#enviando uma pergunta ao gemini e exibindo a resposta
def ask_gemini(question: str) -> str:
    response = model.generate_content(question)
    return response.text
