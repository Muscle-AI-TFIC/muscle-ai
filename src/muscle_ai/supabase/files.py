import json
import os

def sending_information(input_file: str, supabase):

    if not os.path.exists(input_file):
        print(f"Input file {input_file} does not exist.")
        return
    
    with open(input_file, "r", encoding="utf-8") as file:
        training_data = json.load(file)

    if not isinstance(training_data, list) or not training_data:
        print("No data found")
        return

    for entry in training_data:
        user_id = entry.get("user_id")
        training_plan = entry.get("training_plan", {})

        for day_name, exercises in training_plan.items():
            if exercises == "rest" or not exercises:
                continue

            daily_workout_data = {
                "user_id": user_id,
                "workout_date": day_name
            }
            try:
                response = supabase.table("daily_workouts").insert(daily_workout_data).execute()
                daily_workout_id = response.data[0]["id"]
                print(f"  Created daily_workout for {day_name} (ID: {daily_workout_id})")


                exercise_rows = []
                for ex in exercises:
                    exercise_rows.append({
                        "daily_workout_id": daily_workout_id,
                        "exercise_id": ex.get("exercise_id"),
                        "position": ex.get("position"),
                        "sets": ex.get("sets"),
                        "reps": ex.get("reps")
                    })

                if exercise_rows:
                    supabase.table("daily_workout_exercises").insert(exercise_rows).execute()
                    print(f"  Added {len(exercise_rows)} exercises for {day_name}")

            except Exception as e:
                print(f"Failed to sent data (user_id: {user_id}): {e}")

    print("Done mate!")