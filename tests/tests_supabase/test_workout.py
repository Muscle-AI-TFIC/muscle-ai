import pytest
from unittest.mock import Mock, patch
from muscle_ai.supabase.workouts import get_daily_workout

def test_get_daily_workout():

    mock_supabase = Mock()
    mock_response = Mock()

    mock_data = [
        {
            "id": "12",
            "user_id": "user1234",
            "workout_date": "2024-01-15",
        }
    ]
    mock_response.data = mock_data
    mock_supabase.table.return_value.select.return_value.in_.return_value.execute.return_value = mock_response

    result = get_daily_workout(mock_supabase, ["12"])

    assert result == mock_data






