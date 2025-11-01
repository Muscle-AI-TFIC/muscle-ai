import pytest
from unittest.mock import Mock, patch, mock_open
from muscle_ai.get_user import get_user, save_json, initialize_supabase

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


@patch("builtins.open", new_callable=mock_open)
@patch("json.dump")
def test_save_json(mock_json_dump, mock_file):

    data = {"name": "user1234", "idade": "19"}
    filepath = "test.json"

    save_json(data, filepath)

    mock_file.assert_called_once_with(filepath, "w", encoding="utf-8")

    mock_json_dump.assert_called_once_with(data, mock_file(), indent=2, ensure_ascii=False)


@patch("muscle_ai.get_user.create_client")
@patch("builtins.open", new_callable=mock_open, read_data='{"SUPABASE_URL": "url", "SUPABASE_KEY": "key"}')
@patch("os.path.exists", return_value=True)
def test_initialize_supabase_success(mock_exists, mock_open_file, mock_create_client):

    mock_client = Mock()
    mock_create_client.return_value = mock_client
    
    result = initialize_supabase()
    
    mock_create_client.assert_called_once_with("url", "key")
    
    assert result == mock_client

