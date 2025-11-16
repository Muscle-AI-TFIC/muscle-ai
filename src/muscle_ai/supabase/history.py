def saving_history_workouts(workouts:list, exercises:list, supabase):
    print("Saving history workout...")

    for workout in workouts:
        user_id = workout["user_id"]
        workout_id = workout["id"]

        user_exercises = [ex for ex in exercises if ex["daily_workout_id"] == workout_id]

        if user_exercises:
            history_data = [{"user_id": user_id, "exercise_id": ex["exercise_id"]} for ex in user_exercises]
            supabase.table("user_exercise_history").insert(history_data).execute()

        supabase.table("daily_workout_exercises").delete().eq("daily_workout_id", workout_id).execute()
        supabase.table("daily_workouts").delete().eq("id", workout_id).execute()


    print("History workout saving completed.")