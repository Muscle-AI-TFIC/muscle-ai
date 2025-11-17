from unittest.mock import patch
from muscle_ai.ai.generator import generate_training_plan

@patch("muscle_ai.ai.generator.ask_gemini")
def test_generate_training_plan(mock_ask_gemini):
    mock_ask_gemini.return_value = '{"data": {"Monday": []}}'

    traning_data = {
        "age": 25,
        "goal": "muscle gain",
        "weight": 70,
        "height": 175,
        "fitness_level": "intermediate"
    }

    result = generate_training_plan(traning_data)

    assert result == '{"data": {"Monday": []}}'
    mock_ask_gemini.assert_called_once()
