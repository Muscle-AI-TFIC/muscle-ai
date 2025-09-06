import builtins
import pytest
import muscle_ai.main as main

def test_main_normal_flow(monkeypatch, capsys):
    #Simulating the user input
    inputs = iter(["What is the better type of traning to starters?", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    #temporarily replace ask_gemini to generate a fake response
    monkeypatch.setattr("muscle_ai.main.ask_gemini", lambda q: "Leg traning")

    main.main()

    captured = capsys.readouterr()
    assert "Leg traning" in captured.out
