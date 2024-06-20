import requests
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.api import get_data_from_api
@patch('requests.get')
def test_get_data_from_api(mock_get):
    mock_get.return_value.json.return_value = {'key': 'value'}
    data = get_data_from_api('https://jsonplaceholder.typicode.com/todos/1')
    assert data == {'key': 'value'}
