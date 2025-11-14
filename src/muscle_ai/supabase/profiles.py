def get_user(supabase):

    response = supabase.table("user_profiles").select("*").execute()
    profiles = response.data if hasattr(response, "data") else response
 
    user_data = []

    for user in profiles:
        user_data.append({
            "id": user.get("id"),
            "gender": user.get("gender"),
            "weight_kg": user.get("weight_kg"),
            "height_cm": user.get("height_cm"),
            "fitness_level": user.get("fitness_level"),
            "goal": user.get("goal")
        })
    return user_data