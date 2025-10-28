from supabase import create_client, Client
import json
import os

def initialize_supabase():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    cred_path = os.path.join(project_root, "key.json")
        
    if not os.path.exists(cred_path):
        raise FileNotFoundError(f"key.json not found at {cred_path}")
        
    with open(cred_path, "r", encoding="utf-8") as f:
        keys = json.load(f)

    supabase: Client = create_client(keys["SUPABASE_URL"], keys["SUPABASE_KEY"])
    print("Supabase initialized successfully.")
    return supabase



def get_user():

    supabase = initialize_supabase()

    response = supabase.table("person_info").select("*").execute()
    profiles = response.data if hasattr(response, "data") else response
 
    user_data = []

    for user in profiles:
        user_data.append({
            "id": user.get("user_id"),
            "age": user.get("age"),
            "height": user.get("height"),
            "weight": user.get("weight"),
            "goal": user.get("goal")
        })
    return user_data

def save_json(data, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print(f"json file saved on {filepath}")
