import json
from muscle_ai.ai.cleaner import clean_ai_response
from muscle_ai.ai.generator import generate_training_plan
from muscle_ai.core.utils import save_json
import time


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