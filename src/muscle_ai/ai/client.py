from muscle_ai.core.config import Config

def ask_gemini(question: str) -> str:
    model = Config.GEMINI_MODEL_INSTANCE
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        print(f"Error during AI request: {e}")
        return None
