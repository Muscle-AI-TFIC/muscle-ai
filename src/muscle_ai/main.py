from muscle_ai.trainer import load_user_data, generate_training_plan
import json

def save_training_plan(training_plan: str, user_data: dict) -> str:
    
    filename = f"{user_data.get('name', 'user').lower()}_training_plan.json"
    plan_data = {
        "user_name": user_data.get('name', 'User'),
        "training_plan": training_plan
    }
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(plan_data, f, indent=2, ensure_ascii=False)
    
    return filename


def main():
    print("Muscle AI: Thinking about the best type of traning just for you!\n")
    
    user_data = load_user_data("user_data.json")
    training_plan = generate_training_plan(user_data)
    saved_file = save_training_plan(training_plan, user_data)

    print(f"Training plan generated and saved to {saved_file}.")


if __name__ == "__main__":
    main()