import pytest
from unittest.mock import patch, MagicMock
from muscle_ai.get_user import get_user_firebase

def test_user_firebase_mock_empty():

    mock_user_firebase = MagicMock()
    mock_user_firebase.iterate_all.return_value = []

    with patch('firebase_admin.auth.list_users', return_value=mock_user_firebase):

        users = get_user_firebase()
        assert users == [] 

def test_user_firebase_mock_with_users():
    # mockando os usuarios para testar

    mock_user1 = MagicMock()
    mock_user1.uid = "10"
    mock_user1.email = "test1@example.com"
    mock_user1.display_name = "user 1"
    mock_user1.disabled = True
    
    mock_user_list = MagicMock()
    mock_user_list.iterate_all.return_value = [mock_user1] 
    
    with patch('firebase_admin.auth.list_users', return_value=mock_user_list):
        
        users = get_user_firebase()
        
        # verificando se os dados dos usuarios batem com o mock
        assert users[0] == {
            'id': '10',
            'email': 'test1@example.com',
            'name': 'user 1',
            'active': True
        }
