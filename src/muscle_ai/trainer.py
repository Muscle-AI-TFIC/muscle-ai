import json
from muscle_ai.ai_client import ask_gemini

def generate_training_plan(traning_data: dict):
    prompt = (
        f"Generate a weekly gym training plan in English for the following user profile:\n\n"
        f"Age: {traning_data.get('age')}\n"
        f"Goal: {traning_data.get('goal')}\n"
        f"Weight: {traning_data.get('weight')} kg\n"
        f"Height: {traning_data.get('height')} cm\n\n"
        f"Respond ONLY in JSON format with this structure:\n"
        f"data: {{\n"
        f"  'Monday': {{ 'exercises': {{'ExerciseName': repetitions, ... }} }},\n"
        f"  'Tuesday': {{ 'exercises': {{'ExerciseName': repetitions, ... }} }},\n"
        f"  ...\n"
        f"}}\n"
        f"If a day has no exercises, set its value to the string 'rest' instead of an empty object.\n"
        f"Example:\n"
        f"{{\n"
        f"  \"data\": {{\n"
        f"    \"Monday\": {{\"exercises\": {{\"Bench Press\": 12, \"Bicep Curl\": 12}}}},\n"
        f"    \"Tuesday\": \"rest\",\n"
        f"    \"Wednesday\": {{\"exercises\": {{\"Deadlift\": 10}}}}\n"
        f"  }}\n"
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
            "training_plan": plan_data.get("data", {})
        })
                
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
        
    print(f"Json file saved on: {output_file_path}")
    return results
    