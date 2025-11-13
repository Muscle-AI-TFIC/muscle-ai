import json
from muscle_ai.ai_client import ask_gemini
from muscle_ai.get_user import save_json
import time

def generate_training_plan(traning_data: dict):

    prompt = (
    f"Generate a full weekly training plan in English for the following user profile:\n\n"
    f"Age: {traning_data.get('age')}\n"
    f"Goal: {traning_data.get('goal')}\n"
    f"Weight: {traning_data.get('weight')} kg\n"
    f"Height: {traning_data.get('height')} cm\n"
    f"Fitness Level: {traning_data.get('fitness_level', 'beginner')}\n\n"
    f"Available exercises with their IDs (use only these IDs):\n"
    f"1: Push-up, 2: Squat, 3: Plank, 4: Lunges, 5: Crunch,\n"
    f"6: Bench Press, 7: Pull-up, 8: Shoulder Press, 9: Barbell Row, 10: Leg Press,\n"
    f"11: Deadlift, 12: Clean and Press, 13: Weighted Dips, 14: Bulgarian Split Squat, 15: Snatch\n\n"

    f"Respond ONLY in valid JSON format with this structure (no text before or after JSON):\n"
    f"{{\n"
    f"  \"data\": {{\n"
    f"    \"Monday\": [{{\"exercise_id\": 1, \"position\": 1, \"sets\": 3, \"reps\": 12}}],\n"
    f"    \"Tuesday\": [{{\"exercise_id\": 2, \"position\": 1, \"sets\": 3, \"reps\": 10}}],\n"
    f"    \"Wednesday\": \"rest\",\n"
    f"    \"Thursday\": [{{\"exercise_id\": 3, \"position\": 1, \"sets\": 3, \"reps\": 60}}],\n"
    f"    \"Friday\": [{{\"exercise_id\": 4, \"position\": 1, \"sets\": 3, \"reps\": 12}}],\n"
    f"    \"Saturday\": [{{\"exercise_id\": 5, \"position\": 1, \"sets\": 3, \"reps\": 15}}],\n"
    f"    \"Sunday\": \"rest\"\n"
    f"  }}\n"
    f"}}\n\n"

    f"IMPORTANT RULES:\n"
    f"- Each non-rest day MUST be a list of objects.\n"
    f"- Each exercise MUST contain exactly these keys: exercise_id, position, sets, reps.\n"
    f"- 'position' must start at 1 and increase sequentially.\n"
    f"- Use ONLY exercise IDs from the list above (1-15).\n"
    f"- Generate between 3 and 5 exercises for each training day.\n"
    f"- reps = number of repetitions inside each set. Must depend on fitness level:\n"
    f"  - Beginner: 8-12 reps\n"
    f"  - Intermediate: 10-15 reps\n"
    f"  - Advanced: 12-20 reps\n"
    f"- sets = number of sets (blocks) the exercise will be performed. Must be 3 to 5.(integer number only).\n"
    f"- Include at least 1 rest day.\n"
    f"- REMEMBER THE FITNESS LEVEL OF THE USER WHEN CREATING THE PLAN.\n"
    f"- DO NOT include any explanation or commentary outside the JSON.\n"
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

        if not ai_response:
            print(f"Skipping user {user_id}: AI failed to generate a response.")
            continue
        try:
            ai_response_clean = clean_ai_response(ai_response)

            plan_data = json.loads(ai_response_clean)

            training_plan = plan_data.get("data", {})

            results.append({
                "user_id": user_id,
                "training_plan": training_plan
            })
        except Exception as e:
            print(f"Skipping user {user_id}: Invalid JSON returned. Error: {e}")
            continue

        time.sleep(30)
    

    save_json(results, output_file_path)

    return results
    