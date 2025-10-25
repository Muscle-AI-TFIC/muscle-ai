import json
from pathlib import Path
from muscle_ai.ai_client import ask_gemini


def load_user_data(file_path: str) -> dict:

    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File {file_path} not found.")
    
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_training_plan(traning_data: dict) -> str:
    prompt = (
        f"Create the best gym training plan for the following profile:\n\n"
        f"Age: {traning_data.get('idade')}\n"
        f"Goal: {traning_data.get('objetivo')}\n"
        f"Weight: {traning_data.get('peso')} kg\n"
    )
    return ask_gemini(prompt)
