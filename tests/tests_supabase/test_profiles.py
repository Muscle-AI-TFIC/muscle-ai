import pytest
from unittest.mock import Mock, patch, mock_open
from muscle_ai.supabase.profiles import get_user

def test_get_user():

    mock_supabase = Mock()
    mock_response = Mock()

    mock_data = [
        {
            "id": "1",
            "gender": "male",
            "weight_kg": 80,
            "height_cm": 180,
            "fitness_level": "intermediate",
            "goal": "muscle_gain"
        }
    ]

    mock_response.data = mock_data
    mock_supabase.table.return_value.select.return_value.execute.return_value = mock_response

    result = get_user(mock_supabase)

    assert result == mock_data