from flask import Flask
import pytest
import json
import requests

def test_post_success():
    mimetype = 'application/json'
    headers = {
        'Content-Type':mimetype,
    }
    data = {
        'list': [1, 2, 3],
    }

    url = 'http://127.0.0.1:5000/v1.1.0/total'

    

    response = requests.post(url,data = json.dumps(data), headers= headers )
    resp_body = response.json()

    assert response.status_code == 200
    assert response.headers['Content-Type'] == mimetype
    assert resp_body['total'] == 6


