import pytest
from unittest.mock import patch, Mock
import muscle_ai.main as main


def test_save_training_plan():
    user_data = {"name": "Alice"}
    training_plan = "Plan A"
    expected_filename = "alice_training_plan.json"

    mock_file = Mock()
    mock_file.__enter__ = Mock(return_value=mock_file)
    mock_file.__exit__ = Mock(return_value=None)

    with patch("builtins.open", return_value=mock_file):     
        filename = main.save_training_plan(training_plan, user_data)

    #Verifying that the file has the expected name
    assert filename == expected_filename

def test_main(capsys):
    #Mocking the functions called within main()
    with patch("muscle_ai.main.load_user_data") as mock_load, \
         patch("muscle_ai.main.generate_training_plan") as mock_generate, \
         patch("muscle_ai.main.save_training_plan") as mock_save:

        mock_load.return_value = {"name": "TestUser"}
        mock_generate.return_value = "Fake Training Plan"
        mock_save.return_value = "testuser_training_plan.json"

        main.main()

        #Capturing printed output
        captured = capsys.readouterr()
        assert "Muscle AI: Thinking about the best type of traning just for you!" in captured.out
        assert "Training plan generated and saved to testuser_training_plan.json." in captured.out