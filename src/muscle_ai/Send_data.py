from muscle_ai.get_user import initialize_supabase
import json
import os

def sending_information(input_file: str):

    if not os.path.exists(input_file):
        print(f"Input file {input_file} does not exist.")
        return
    
    with open(input_file, "r", encoding="utf-8") as file:
        training_data = json.load(file)

    if not isinstance(training_data, list) or not training_data:
        print("No data found")
        return

    supabase = initialize_supabase()

    for entry in training_data:
        user_id = entry.get("user_id")
        training_plan = entry.get("training_plan", {})

        data_to_insert = {
            "user_id": user_id,
            "monday": training_plan.get("Monday", {}),
            "tuesday": training_plan.get("Tuesday", {}),
            "wednesday": training_plan.get("Wednesday", {}),
            "thursday": training_plan.get("Thursday", {}),
            "friday": training_plan.get("Friday", {}),
            "saturday": training_plan.get("Saturday", {}),
            "sunday": training_plan.get("Sunday", {}),
        }

        try:
            response = supabase.table("training_ai").insert(data_to_insert).execute()
            print(f"Datas sent (user_id: {user_id})")
        except Exception as e:
            print(f"Failed to sent data (user_id: {user_id}): {e}")