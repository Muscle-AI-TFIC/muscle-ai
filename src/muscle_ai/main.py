from muscle_ai.trainer import load_user_data, generate_training_plan
from muscle_ai.get_user import get_user_firebase, save_json, get_traning_firebase

import time
import os

def main():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    output_fileUser = os.path.join(project_root, "user.json")
    output_fileTraning = os.path.join(project_root, "training.json")

    try:
        while True:
            user_data = get_user_firebase()
            save_json(user_data, output_fileUser)

            training_data = get_traning_firebase()
            save_json(training_data, output_fileTraning)
            
            time.sleep(60)
    except KeyboardInterrupt:
        print("Ending the program.")


if __name__ == "__main__":
    main()