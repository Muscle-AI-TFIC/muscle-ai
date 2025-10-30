import pytest
from unittest.mock import Mock, patch
from muscle_ai.get_daily_workout import get_daily_workout_exercises
from muscle_ai.get_daily_workout import get_daily_workout

@patch("muscle_ai.get_daily_workout.initialize_supabase")
def test_get_daily_workout_success(mock_initialize_supabase):

    mock_supabase = Mock()
    mock_response = Mock()

    mock_data = [
        {
            "id": "12",
            "user_id": "Fuad123",
            "workout_date": "2024-01-15",
        }
    ]

    mock_response.data = mock_data
    mock_supabase.table.return_value.select.return_value.execute.return_value = mock_response

    mock_initialize_supabase.return_value = mock_supabase

    result = get_daily_workout()

    expected = [
        {
            "id": "12",
            "user_id": "Fuad123",
            "workout_date": "2024-01-15",
        }
    ]

    assert result == expected

@patch("muscle_ai.get_daily_workout.initialize_supabase")
def test_get_daily_workout_exercises_success(mock_initialize_supabase):

    mock_supabase = Mock()
    mock_response = Mock()

    mock_data = [
        {
             "id" : "62" , 
            "daily_workout_id": "19" , 
            "exercise_id": "6"  , 
        }
    ]

    mock_response.data = mock_data
    mock_supabase.table.return_value.select.return_value.execute.return_value = mock_response

    mock_initialize_supabase.return_value = mock_supabase

    result = get_daily_workout_exercises()

    expected = [
        {
             "id": "62", 
            "daily_workout_id": "19", 
            "exercise_id": "6", 
        }
    ]

    assert result == expected




