import json
from muscle_ai.ai_client import ask_gemini
from muscle_ai.get_user import save_json
from datetime import datetime
import time

def get_current_day():
    return datetime.now().strftime("%A")

def generate_training_plan(traning_data: dict):

    current_day = get_current_day()

    prompt = (
        f"Generate a {current_day} training plan in English for the following user profile:\n\n"
        f"Age: {traning_data.get('age')}\n"
        f"Goal: {traning_data.get('goal')}\n"
        f"Weight: {traning_data.get('weight')} kg\n"
        f"Height: {traning_data.get('height')} cm\n"
        f"Fitness Level: {traning_data.get('fitness_level', 'beginner')}\n\n"
        f"Available exercises with their IDs:\n"
        f"1: Push-up, 2: Squat, 3: Plank, 4: Lunges, 5: Crunch,\n"
        f"6: Bench Press, 7: Pull-up, 8: Shoulder Press, 9: Barbell Row, 10: Leg Press,\n"
        f"11: Deadlift, 12: Clean and Press, 13: Weighted Dips, 14: Bulgarian Split Squat, 15: Snatch\n\n"
        f"Respond ONLY in JSON format with this structure:\n"
        f"{{\n"
        f"  \"data\": {{\n"
        f"    \"Monday\": [\n"
        f"      {{\"exercise_id\": 1, \"position\": 1, \"sets\": 3, \"reps\": 12}},\n"
        f"      {{\"exercise_id\": 2, \"position\": 2, \"sets\": 3, \"reps\": 10}},\n"
        f"      {{\"exercise_id\": 3, \"position\": 3, \"sets\": 3, \"reps\": 60}}\n"
        f"    ]\n"
        f"  }}\n"
        f"}}\n"
        f"Important rules:\n"
        f"- Use ONLY the exercise IDs from the list above (1-15)\n"
        f"- 'position' must be sequential starting from 1\n"
        f"- 'sets' should be between 2-5\n"
        f"- 'reps' should be appropriate for the exercise and fitness level\n"
        f"- For Plank (ID 3), reps represent seconds (e.g., 60 seconds)\n"
        f"- Generate 3-5 exercises for Monday\n"
        f"- Consider the user's fitness level when selecting exercises\n"
        f"- Make sure the plan aligns with the user's goal\n"
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
    current_day = get_current_day()
        
    for user in training_file:
        user_id = user.get('id')

        print(f"Processing training plan for user ID: {user_id}")

        ai_response = generate_training_plan(user)
        ai_response_clean = clean_ai_response(ai_response)

        plan_data = json.loads(ai_response_clean)

        training_plan = {
            current_day: plan_data.get("data", {}).get(current_day, [])
        }

        results.append({
            "user_id": user_id,
            "training_plan": training_plan
        })

        time.sleep(30)
    

    save_json(results, output_file_path)

    return results
    