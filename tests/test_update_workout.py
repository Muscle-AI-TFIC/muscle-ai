import pytest
from unittest.mock import Mock, patch
from muscle_ai.update_workout import saving_history_workouts


@patch("muscle_ai.update_workout.initialize_supabase")
def test_saving_history_workouts(mock_initialize_supabase):

    mock_supabase = Mock()
    mock_initialize_supabase.return_value = mock_supabase

    mock_table = Mock()
    mock_supabase.table.return_value = mock_table

    workouts = [
        {
            "user_id": "user_123",
            "id": "19", 
        }
    ]
    exercises = [
        {
            "daily_workout_id": "19", 
            "exercise_id": "2" ,
         }
    ]

    saving_history_workouts(workouts=workouts, exercises=exercises)

    mock_supabase.table.assert_any_call("user_exercise_history")
    mock_supabase.table.assert_any_call("daily_workout_exercises")
    mock_supabase.table.assert_any_call("daily_workouts")
