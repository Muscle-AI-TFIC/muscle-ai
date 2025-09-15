import pytest
import json
from unittest.mock import patch, mock_open
from muscle_ai import trainer


def test_generate_training_plan_with_mock():
    #Simulating the user data
    fake_user_data = {
        'age': 25,
        'weight': 70,
        'height': 1.75,
        'objective': 'get stronger',
        'level': 'starter',
        'language': 'portuguese'
    }

    #Simulating a fake response from the AI
    fake_response = "Fake traning"

    #Mocking the ask_gemini function to return the fake response
    with patch("muscle_ai.trainer.ask_gemini", return_value=fake_response) as mock_ai:

        result = trainer.generate_training_plan(fake_user_data)

        assert result == fake_response


def test_load_user_data_with_mock():
    #Simulating the content of a Json file
    fake_json = json.dumps({
        'age': 30,
        'weight': 80,
        'height': 1.80,
        'objective': 'lose weight',
        'level': 'starter',
        'language': 'portuguese'
    })

     #Mocking the Path.exists method to always return True or the test will fail
    with patch("pathlib.Path.exists", return_value=True):
        #Mocking the open function to simulate reading from a file
        with patch("builtins.open", mock_open(read_data=fake_json)):
            data = trainer.load_user_data("fake_path.json")

            assert data['age'] == 30
            assert data['weight'] == 80
            assert data['objective'] == 'lose weight'
