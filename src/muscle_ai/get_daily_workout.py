from muscle_ai.get_user import initialize_supabase

def get_daily_workout():

    supabase = initialize_supabase()

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

def get_daily_workout_exercises():

    supabase = initialize_supabase()

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

