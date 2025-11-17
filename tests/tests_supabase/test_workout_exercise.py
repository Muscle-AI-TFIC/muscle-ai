import pytest
from unittest.mock import Mock, patch
from muscle_ai.supabase.workout_exercise import get_daily_workout_exercises

def test_get_daily_workout_exercises():

    mock_supabase = Mock()
    mock_response = Mock()

    mock_data = [
        {
            "id": "62",
            "daily_workout_id": "19",
            "exercise_id": "6",
        }
    ]

    mock_response.data = mock_data
    mock_supabase.table.return_value.select.return_value.execute.return_value = mock_response

    result = get_daily_workout_exercises(mock_supabase)

    assert result == mock_data