import pytest
import json
from unittest.mock import patch, Mock
from muscle_ai import trainer


def test_generate_training_plan():
    #Simulating the user data
    fake_user_data = {
        'name': 'Caio',
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
    with patch("muscle_ai.trainer.ask_gemini", return_value=fake_response):

        result = trainer.generate_training_plan(fake_user_data)

        assert result == fake_response


def test_load_user_data():
    #Simulating JSON
    fake_json = json.dumps({
        'name': 'Caio',
        'age': 30,
        'weight': 80,
        'height': 1.80,
        'objective': 'lose weight',
        'level': 'starter',
        'language': 'portuguese'
    })

    #Criating a mock to simulate the file
    mock_file = Mock()
    mock_file.__enter__ = Mock(return_value=mock_file)
    mock_file.__exit__ = Mock(return_value=None)
    mock_file.read = Mock(return_value=fake_json)

    #Mocking the Path.exists method to always return True or the test will fail
    with patch("pathlib.Path.exists", return_value=True):
        #Opening the mock file instead of a real file
        with patch("builtins.open", return_value=mock_file):
            data = trainer.load_user_data("fake_path.json")

            assert data['age'] == 30
            assert data['weight'] == 80
            assert data['objective'] == 'lose weight'
