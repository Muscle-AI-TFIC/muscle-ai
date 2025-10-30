from muscle_ai.trainer import process_training_plans
from muscle_ai.get_user import get_user, save_json
from muscle_ai.Send_data import sending_information
from muscle_ai.get_daily_workout import get_daily_workout, get_daily_workout_exercises
from muscle_ai.update_workout import saving_history_workouts

import os

def main():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    output_fileUser = os.path.join(project_root, "user.json")
    output_fileTraningAi = os.path.join(project_root, "traningAi.json")
    output_filedaily_workout = os.path.join(project_root, "daily_workout.json")
    output_filedaily_workout_exercises = os.path.join(project_root, "daily_workout_exercises.json")


    user_data = get_user()
    daily_workout_data = get_daily_workout()
    daily_workout_exercises_data = get_daily_workout_exercises()
    save_json(daily_workout_data, output_filedaily_workout)
    save_json(daily_workout_exercises_data, output_filedaily_workout_exercises)
    save_json(user_data, output_fileUser)
    saving_history_workouts(daily_workout_data, daily_workout_exercises_data)
    process_training_plans(user_data, output_fileTraningAi)
    sending_information(output_fileTraningAi)

            


if __name__ == "__main__":
    main()