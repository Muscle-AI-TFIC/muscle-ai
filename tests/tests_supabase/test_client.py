import pytest
from unittest.mock import Mock, patch
from muscle_ai.supabase.client import get_supabase

def test_get_supabase_initializes_client():
    mock_client_instance = Mock()

    with patch("muscle_ai.supabase.client.create_client", return_value=mock_client_instance) as mock_create:

        result = get_supabase()

        mock_create.assert_called_once()

        assert result is mock_client_instance
