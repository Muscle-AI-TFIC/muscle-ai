def get_daily_workout(supabase):

    response = supabase.table("daily_workouts").select("*").execute()
    profiles = response.data if hasattr(response, "data") else response
 
    workout_data = []

    for workout in profiles:
        workout_data.append({
            "id": workout.get("id"),
            "user_id": workout.get("user_id"),
            "workout_date": workout.get("workout_date")
        })
    return workout_data