import pytest
import json
from unittest.mock import patch
from main import fetch_fbi_wanted_data

@pytest.fixture
def mock_api_response():

    return {
        "items": [
            {"title": "Wanted Person 1", "subjects": ["Subject A", "Subject B"], "field_offices": ["New York", "Los Angeles"]}
        ]
    }


def test_fetch_fbi_wanted_data(mock_api_response):
    
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.content = json.dumps(mock_api_response).encode('utf-8')
        data = fetch_fbi_wanted_data(page=1)
        assert data['items'], "API returned empty data"
        assert isinstance(data, dict), "data should be a dictionary"
