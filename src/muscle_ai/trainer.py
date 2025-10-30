import json
from muscle_ai.ai_client import ask_gemini

def generate_training_plan(traning_data: dict):
    prompt = (
        f"Generate a concise gym training summary in English for the following user profile:\n\n"
        f"Age: {traning_data.get('age')}\n"
        f"Goal: {traning_data.get('goal')}\n"
        f"Weight: {traning_data.get('weight')} kg\n"
        f"Height: {traning_data.get('height')} cm\n\n"
        f"Respond ONLY in JSON format with these exact keys:\n"
        f"training_type (string), sets (string), days (string), equipment (string), focus (string).\n"
        f"Example:\n"
        f"{{\n"
        f"  \"training_type\": \"Strength and endurance\",\n"
        f"  \"sets\": \"8 sets\",\n"
        f"  \"days\": \"5 days per week\",\n"
        f"  \"equipment\": \"dumbbells, barbell, bench\",\n"
        f"  \"focus\": \"chest, shoulders, triceps\"\n"
        f"}}"
    )
    return ask_gemini(prompt)

def clean_ai_response(ai_response: str):

    cleaned = ai_response.strip()

    if "{" in cleaned and "}" in cleaned:
        start = cleaned.find("{")
        end = cleaned.rfind("}") + 1
        cleaned = cleaned[start:end]

    return cleaned


def process_training_plans(training_file: list, output_file_path: str):

    print("Generating training plans using AI...")
    results = []
        
    for user in training_file:
        user_id = user.get('id')

        print(f"Processing training plan for user ID: {user_id}")

        ai_response = generate_training_plan(user)
        ai_response_clean = clean_ai_response(ai_response)

        plan_data = json.loads(ai_response_clean)

        results.append({
            "user_id": user_id,
            "training_type": plan_data.get("training_type", ""),
            "sets": plan_data.get("sets", ""),
            "days": plan_data.get("days", ""),
            "equipment": plan_data.get("equipment", ""),
            "focus": plan_data.get("focus", "")
        })
                
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
        
    print(f"Json file saved on: {output_file_path}")
    return results
    