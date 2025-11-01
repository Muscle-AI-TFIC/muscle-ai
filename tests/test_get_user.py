import pytest
from unittest.mock import Mock, patch
from muscle_ai.get_user import get_user

@patch("muscle_ai.get_user.initialize_supabase")
def test_get_user(mock_initialize_supabase):

    mock_supabase = Mock()
    mock_response = Mock()

    mock_data = [
        {
            "id": "1234" ,
            "gender": "M" , 
            "weight_kg": "80" , 
            "height_cm":  "1.80" , 
            "fitness_level": "intermediario" , 
            "goal": "Ganhar massa" , 
        }
    ]

    mock_response.data = mock_data
    mock_supabase.table.return_value.select.return_value.execute.return_value = mock_response

    mock_initialize_supabase.return_value = mock_supabase

    result = get_user()

    expected = [
        {
            "id": "1234" ,
            "gender": "M" , 
            "weight_kg": "80" , 
            "height_cm":  "1.80" , 
            "fitness_level": "intermediario" , 
            "goal": "Ganhar massa" , 
        }
    ]

    assert result == expected
