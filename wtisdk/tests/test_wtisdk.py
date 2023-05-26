import json
from wtisdk import WtiClient
#from unittest.mock import Mock
import pytest
import requests

def test_get_status(mocker):
    # Load the mock response data from the JSON file
    with open('wtisdk/tests/fixtures/wti_get_status.json', 'r') as file:
        mock_response_data = json.load(file)
    
    # Mock the requests library and the response object
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_response_data
    mocker.patch('requests.get', return_value=mock_response)
    
    # Create an instance of the WtiClient class
    client = WtiClient("10.20.30.139", "mteke", "password")
    
    # Call the get_status method
    result = client.get_status()
    
    # Assert the result matches the expected data
    assert result == mock_response_data

    
def test_get_alarm_status(mocker):
    # Load the mock response data from the JSON file
    with open('wtisdk/tests/fixtures/wti_get_alarm_status.json', 'r') as file:
        mock_response_data = json.load(file)

    # Mock the requests library and the response object
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response.json = lambda: mock_response_data
    mocker.patch('requests.get', return_value=mock_response)

    # Create an instance of the WtiClient class
    client = WtiClient("10.20.30.139", "mteke", "password")

    # Call the get_alarm_status method
    result = client.get_alarm_status()

    # Assert the result matches the expected data
    assert result == mock_response_data
