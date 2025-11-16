import json
import pytest
from unittest.mock import patch, MagicMock

from muscle_ai.ai.processing import process_training_plans


@patch("muscle_ai.ai.processing.save_json")
@patch("muscle_ai.ai.processing.time.sleep")
@patch("muscle_ai.ai.processing.clean_ai_response")
@patch("muscle_ai.ai.processing.generate_training_plan")

def test_process_training_plans(
    mock_generate_training,
    mock_clean,
    mock_sleep,
    mock_save_json
):
    
    mock_generate_training.return_value = '{"data": {"Monday": ["Bench Press"]}}'
    mock_clean.return_value = '{"data": {"Monday": ["Bench Press"]}}'

    users = [
        {"id": 1, "age": 25},
        {"id": 2, "age": 30}
    ]

    result = process_training_plans(users, "output.json")

    assert len(result) == 2

    assert result[0]["user_id"] == 1
    assert result[0]["training_plan"] == {"Monday": ["Bench Press"]}

    assert result[1]["user_id"] == 2
    assert result[1]["training_plan"] == {"Monday": ["Bench Press"]}

    mock_save_json.assert_called_once()