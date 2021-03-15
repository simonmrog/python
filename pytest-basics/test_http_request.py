import json
import requests


def test_api_response():
    url = "http://reqres.in/api/users"
    response = requests.get(url)
    users = json.loads(response.text)
    assert response.status_code == 200
    assert users["data"] != None
