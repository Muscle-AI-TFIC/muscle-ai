import json
from pathlib import Path
from muscle_ai.ai_client import ask_gemini


def load_user_data(file_path: str) -> dict:
    #Getting the users information from the json file
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File {file_path} not found.")
    
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_training_plan(user_data: dict) -> str:
    #Sending the users information to the ai model to generate a training plan
    prompt = (
        f"Create the best gym training plan for the following profile:\n\n"
        f"Name: {user_data.get('name')}\n"
        f"Age: {user_data.get('age')}\n"
        f"Weight: {user_data.get('weight')} kg\n"
        f"Height: {user_data.get('height')} m\n"
        f"Goal: {user_data.get('objective')}\n"
        f"Experience level: {user_data.get('level')}\n"
        f"Preferred language: {user_data.get('language')}\n"
    )
    return ask_gemini(prompt)
