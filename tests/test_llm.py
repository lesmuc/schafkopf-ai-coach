from unittest.mock import patch, Mock
from app.llm import generate

def test_generate_returns_response_text():
    mock_response = Mock()
    mock_response.json.return_value  = {"response": "Servus!"}
    mock_response.raise_for_status = Mock()

    with patch("app.llm.requests.post", return_value=mock_response) as mock_post:
        result = generate("Sag Hallo")

    assert result == "Servus!"
    mock_post.assert_called_once()    


