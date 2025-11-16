import pytest
from unittest.mock import Mock
from muscle_ai.supabase.history import saving_history_workouts


def test_saving_history_workouts():
    mock_supabase = Mock()

    workouts = [{"id": "10", "user_id": "user1"}]
    exercises = [
        {"daily_workout_id": "10", "exercise_id": "A"},
        {"daily_workout_id": "99", "exercise_id": "X"},
    ]

    mock_supabase.table.return_value.insert.return_value.execute.return_value = Mock()
    mock_supabase.table.return_value.delete.return_value.eq.return_value.execute.return_value = Mock()

    saving_history_workouts(workouts, exercises, mock_supabase)

    mock_supabase.table("user_exercise_history").insert.assert_called_once_with(
        [{"user_id": "user1", "exercise_id": "A"}]
    )

    mock_supabase.table("daily_workout_exercises").delete.return_value.eq.assert_any_call(
        "daily_workout_id", "10")
    
    mock_supabase.table("daily_workouts").delete.return_value.eq.assert_any_call(
        "id", "10")
