from muscle_ai.core.config import config
from muscle_ai.core.utils import save_json
from muscle_ai.supabase.client import get_supabase
from muscle_ai.supabase.profiles import get_user
from muscle_ai.supabase.workouts import get_daily_workout
from muscle_ai.supabase.workout_exercise import get_daily_workout_exercises
from muscle_ai.ai.processing import process_training_plans


import os

def main():

    config()

    supabase = get_supabase()


    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    output_fileUser = os.path.join(project_root, "user.json")
    output_fileTraningAi = os.path.join(project_root, "traningAi.json")
    output_filedaily_workout = os.path.join(project_root, "daily_workout.json")
    output_filedaily_workout_exercises = os.path.join(project_root, "daily_workout_exercises.json")


    user_data = get_user(supabase)
    daily_workout_data = get_daily_workout(supabase)
    daily_workout_exercises_data = get_daily_workout_exercises(supabase)
    save_json(daily_workout_data, output_filedaily_workout)
    save_json(daily_workout_exercises_data, output_filedaily_workout_exercises)
    save_json(user_data, output_fileUser)
    process_training_plans(user_data, output_fileTraningAi)

if __name__ == "__main__":
    main()