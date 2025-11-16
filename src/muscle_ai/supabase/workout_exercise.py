def get_daily_workout_exercises(supabase):

    response = supabase.table("daily_workout_exercises").select("*").execute()
    profiles = response.data if hasattr(response, "data") else response
 
    workout_data_exercise = []

    for workout in profiles:
        workout_data_exercise.append({
            "id": workout.get("id"),
            "daily_workout_id": workout.get("daily_workout_id"),
            "exercise_id": workout.get("exercise_id"),
        })
    return workout_data_exercise