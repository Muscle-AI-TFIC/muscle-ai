import pytest
from unittest.mock import mock_open, Mock, patch
from muscle_ai.core.utils import save_json
import json

def test_save_json():
    data = {"x": 1}
    fake_path = "file.json"

    with patch("builtins.open", mock_open()) as m, \
         patch("json.dump") as dump_mock:

        save_json(data, fake_path)

        m.assert_called_once_with(fake_path, "w", encoding="utf-8")
        dump_mock.assert_called_once()