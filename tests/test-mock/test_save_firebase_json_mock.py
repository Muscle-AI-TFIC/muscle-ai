import pytest
from unittest.mock import MagicMock, patch, mock_open
from muscle_ai.get_user import save_user_json
import json 

def test_save_user_json_empty():

    user_data = []
    filepath = "test.json"

    with patch("json.dump") as mock_dump:

        save_user_json(user_data, filepath)

        assert user_data == []

def test_save_user_json():

    mock_user_file_save1 = MagicMock()    
    mock_user_file_save1.uid = "12"
    mock_user_file_save1.email = "testes123@gmail.com"
    mock_user_file_save1.display_name = "test 1" 
    mock_user_file_save1.disable = True


    #  Criado para testar se o teste vai falhar caso eu passe esse usuario para comparacao
    mock_user_file_save2 = MagicMock()    
    mock_user_file_save2.uid = "999"
    mock_user_file_save2.email = "testes123@gmail.com"
    mock_user_file_save2.display_name = "test 1" 
    mock_user_file_save2.disable = True


    user_list = [mock_user_file_save1] 
    file_path = 'test.json'

    m = mock_open()

    with patch ("builtins.open", m):

        with patch("json.dump") as mock_dump:
            save_user_json(user_list, file_path)

        m.assert_called_once_with("test.json" , "w" , encoding = 'utf-8')

        actual_data_passed = mock_dump.call_args[0][0]

        assert actual_data_passed == [mock_user_file_save1]




   