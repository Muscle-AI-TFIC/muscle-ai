import pytest
from unittest.mock import patch, mock_open
from muscle_ai.get_user import save_user_json
import json


def test_save_user_json_empty():
    user_data = []
    filepath = "test.json"

    m = mock_open()
    with patch("builtins.open", m), patch("json.dump") as mock_dump:
        save_user_json(user_data, filepath)

        m.assert_called_once_with("test.json", "w", encoding="utf-8")
        mock_dump.assert_called_once_with(user_data, m(), indent=2, ensure_ascii=False)
        assert user_data == []


def test_save_user_json():
    # Simulating user data to be saved
    mock_user_file_save1 = {
        "id": "12",
        "email": "test123@gmail.com",
        "name": "test 1",
        "active": True,
    }

    user_list = [mock_user_file_save1]
    file_path = "test.json"

    m = mock_open()
    with patch("builtins.open", m), patch("json.dump") as mock_dump:
        save_user_json(user_list, file_path)

        actual_data_passed = mock_dump.call_args[0][0]

        assert actual_data_passed == user_list
