'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'TestSecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzA4MDMxNDksIm5iZiI6MTYyOTU5MzU0OSwiZW1haWwiOiJKYWxhbEFsN21hckB0dXJreS5hbDdsb28ifQ.6Hmw3iPmTmX60rrYKw9tbuJ8AlqVGzq3teU4cgBMpDs'
EMAIL = 'JalalAl7mar@turky.al7loo'
PASSWORD = 'jlo'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'
    # assert False

def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None


