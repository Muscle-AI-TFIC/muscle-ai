import pytest
from muscle_ai.ai_client import ask_gemini

def test_ask_gemini(mocker):

    #simulating the response that model.generate_content(question) would return
    TestResponse = type("TestResponse", (), {"text": "test answer"})


    #temporarily replace the model.generate_content function, now it returns TestResponse instead
    mocker.patch("muscle_ai.ai_client.model.generate_content", return_value=TestResponse)
    

    question = "What is the best exercice to the arms?"
    answer = ask_gemini(question)
    

    #checks if the answer is the same as the test one
    assert answer == "test answer"
