# tests/test_main.py
from ai_gateway.main import resolve_provider
from ai_gateway.providers.gemini import GeminiAdapter
import pytest

def test_gemini_model_resolves_to_gemini_adapter():
    # Arrange
    model = "gemini-3.6-flash"

    # Act
    result = resolve_provider(model)

    # Assert
    assert result is GeminiAdapter

'''can use this command in terminal 
uv run pytest tests/test_providers.py -v'''