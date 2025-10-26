import json
from muscle_ai.ai_client import ask_gemini

def generate_training_plan(traning_data: dict) -> str:
    prompt = (
        f"Create the best gym training plan for the following profile:\n\n"
        f"Age: {traning_data.get('age')}\n"
        f"Goal: {traning_data.get('goal')}\n"
        f"Weight: {traning_data.get('weight')} kg\n"
        f"Height: {traning_data.get('height')} cm\n\n"
    )
    return ask_gemini(prompt)

def process_training_plans(training_file: list, output_file_path: str):

    print("Generating training plans using AI...")
    results = []
        
    for user in training_file:
        user_id = user.get('id')

        print(f"Processing training plan for user ID: {user_id}")

        ai_response = generate_training_plan(user)
        
        results.append({
            "user_id": user_id,
            "training_plan": ai_response
        })
                
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
        
    print(f"Json file saved on: {output_file_path}")
    return results
    