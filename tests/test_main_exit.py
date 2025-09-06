import builtins
import pytest
import muscle_ai.main as main


def test_main_exit(monkeypatch, capsys):
    #Simulating that the user typed "exit"
    monkeypatch.setattr(builtins, "input", lambda _: "exit")

    main.main()

    captured = capsys.readouterr()
    assert "Shutting down..." in captured.out
