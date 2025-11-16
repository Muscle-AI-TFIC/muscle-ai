from unittest.mock import patch
from muscle_ai.trainer import get_current_day, clean_ai_response,generate_training_plan, process_training_plans

@patch("muscle_ai.trainer.datetime")

def test_get_current_day(mock_datetime):

    mock_datetime.now.return_value.strftime.return_value = "Monday"
    result = get_current_day()
    assert result == "Monday"
    mock_datetime.now.assert_called_once()


def test_clean_ai_response():

    response = "Some text before {\"data\": {}} some after"

    cleaned = clean_ai_response(response)
    assert cleaned == "{\"data\": {}}"



@patch("muscle_ai.trainer.ask_gemini")
@patch("muscle_ai.trainer.get_current_day", return_value="Monday")

def test_generate_training_plan(mock_day, mock_ask_gemini):
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


@patch("muscle_ai.trainer.time.sleep", return_value=None)
@patch("muscle_ai.trainer.save_json")
@patch("muscle_ai.trainer.clean_ai_response", return_value='{"data": {"Monday": []}}')
@patch("muscle_ai.trainer.generate_training_plan", return_value='{"data": {"Monday": []}}')
@patch("muscle_ai.trainer.get_current_day", return_value="Monday")

def test_process_training_plans(mock_day, mock_generate, mock_clean, mock_save, mock_sleep):
    users = [
        {
            "id": "user123"
        }
    ]
    
    output_file = "fake_output.json"

    result = process_training_plans(users, output_file)

    assert result == [{
        "user_id": "user123",
        "training_plan": {"Monday": []}
    }]

