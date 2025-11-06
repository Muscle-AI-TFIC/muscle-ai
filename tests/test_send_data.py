import pytest
from unittest.mock import Mock, patch, mock_open
from muscle_ai.Send_data import sending_information
import json

@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open)
@patch("muscle_ai.Send_data.initialize_supabase")

def test_sending_information(mock_init_supabase, mock_file, mock_exists):

    fake_data = [
        {
            "user_id": "user_id" , 
            "training_plan": {
                "monday": [
                    {"exercise_id": 1, "position": 1, "sets": 3, "reps": 10},
                    {"exercise_id": 2, "position": 2, "sets": 4, "reps": 8}
                ],
                "tuesday": "rest" 
            }
        }
    ]

    mock_file.return_value.read.return_value = json.dumps(fake_data)

    mock_supabase = Mock()
    mock_response = Mock()
    mock_response.data = [{"id": 12}]

    mock_supabase.table.return_value.insert.return_value.execute.return_value = mock_response
    mock_init_supabase.return_value = mock_supabase

    sending_information("fake_file.json")

    mock_init_supabase.assert_called_once()
    mock_supabase.table.assert_any_call("daily_workouts")
    mock_supabase.table.assert_any_call("daily_workout_exercises")

