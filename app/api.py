import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout
from flask import jsonify

def get_data_from_api(api_url):
    response = requests.get(api_url)
    response.raise_for_status()  # This will raise an exception for HTTP errors
    return response.json()
