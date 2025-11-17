import pytest
from unittest.mock import Mock,patch
from muscle_ai.ai.client import ask_gemini
from muscle_ai.core.config import Config

def test_ask_gemini():
    
    mock_model = Mock()
    mock_response = Mock()
    mock_response.text = "AI answer"
    mock_model.generate_content.return_value = mock_response

    with patch.object(Config, "GEMINI_MODEL_INSTANCE", mock_model):
        result = ask_gemini("test")

    assert result == "AI answer"
    mock_model.generate_content.assert_called_once_with("test")


def test_ask_gemini_error():

    mock_model = Mock()
    mock_model.generate_content.side_effect = Exception("error")

    with patch.object(Config, "GEMINI_MODEL_INSTANCE", mock_model):
        result = ask_gemini("Hello?")

    assert result is None
    mock_model.generate_content.assert_called_once_with("Hello?")
