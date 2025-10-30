import pytest
from muscle_ai.ai_client import ask_gemini

def test_ask_gemini(mocker):

    TestResponse = type("TestResponse", (), {"text": "test answer"})

    mocker.patch("muscle_ai.ai_client.model.generate_content", return_value=TestResponse)
    

    question = "What is the best exercice to the arms?"
    answer = ask_gemini(question)
    
    assert answer == "test answer"
