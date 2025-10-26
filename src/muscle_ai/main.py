from muscle_ai.trainer import process_training_plans
from muscle_ai.get_user import get_user, save_json
from muscle_ai.Send_data import sending_information

import time
import os

def main():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    output_fileUser = os.path.join(project_root, "user.json")
    output_fileTraningAi = os.path.join(project_root, "traningAi.json")

    try:
        while True:
            user_data = get_user()
            save_json(user_data, output_fileUser)
            process_training_plans(user_data, output_fileTraningAi)
            sending_information(output_fileTraningAi)
            
            time.sleep(240)
    except KeyboardInterrupt:
        print("Ending the program.")


if __name__ == "__main__":
    main()