import json
from unittest.mock import Mock, patch, mock_open
from muscle_ai.supabase.files import sending_information


def test_sending_information_success():

    fake_json = json.dumps([
        {
            "user_id": "user1",
            "training_plan": {
                "2024-01-10": [
                    {
                        "exercise_id": "55",
                        "position": 1,
                        "sets": 3,
                        "reps": 10
                    }
                ]
            }
        }
    ])

    mock_supabase = Mock()

    mock_table_daily = Mock()
    mock_table_exercises = Mock()

    mock_supabase.table.side_effect = lambda name: {
        "daily_workouts": mock_table_daily,
        "daily_workout_exercises": mock_table_exercises,
    }[name]

    mock_insert_workout_response = Mock()
    mock_insert_workout_response.data = [{"id": "100"}]
    mock_table_daily.insert.return_value.execute.return_value = mock_insert_workout_response

    mock_table_exercises.insert.return_value.execute.return_value = Mock()

    with patch("builtins.open", mock_open(read_data=fake_json)):
        with patch("os.path.exists", return_value=True):
            sending_information("fake.json", mock_supabase)

    mock_table_daily.insert.assert_called_once_with({
        "user_id": "user1",
        "workout_date": "2024-01-10"
    })

    mock_table_exercises.insert.assert_called_once_with([
        {
            "daily_workout_id": "100",
            "exercise_id": "55",
            "position": 1,
            "sets": 3,
            "reps": 10
        }
    ])
