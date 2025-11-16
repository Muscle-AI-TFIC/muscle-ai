import os
from unittest.mock import patch
from muscle_ai.main import main  

@patch("muscle_ai.main.sending_information")
@patch("muscle_ai.main.process_training_plans")
@patch("muscle_ai.main.saving_history_workouts")
@patch("muscle_ai.main.save_json")
@patch("muscle_ai.main.get_daily_workout_exercises", return_value=[{"ex": "ok"}])
@patch("muscle_ai.main.get_daily_workout", return_value=[{"dw": "ok"}])
@patch("muscle_ai.main.get_user", return_value=[{"id": "user123"}])
@patch("muscle_ai.main.os.path.dirname", side_effect=lambda path=None: "/fakepath")
@patch("muscle_ai.main.os.path.abspath", return_value="/fakepath/main.py")

def test_main_function(
    mock_abspath,
    mock_dirname,
    mock_get_user,
    mock_get_daily_workout,
    mock_get_daily_exercises,
    mock_save_json,
    mock_save_history,
    mock_process_plans,
    mock_send_info
):

    main()

    assert mock_save_json.call_count == 3 