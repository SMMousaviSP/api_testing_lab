import requests
import pytest

from local_config import TOKEN

BASE_URL = "https://api.gitter.im"


@pytest.fixture
def header():
    return {'Authorization': 'Bearer ' + TOKEN}


@pytest.mark.status_code
def test_user_header(header):
    response = requests.get(BASE_URL+'/v1/user', headers=header)
    assert response.status_code==200

def test_user_type(header):
    response = requests.get(BASE_URL+'/v1/user', headers=header)
    assert type(response.json()[0]['displayName'])==str

def test_user_content(header):
    response = requests.get(BASE_URL+'/v1/user', headers=header)
    assert response.json()[0]['displayName']=="Célia Fritsch" #replace with your name

def test_get_check_content_type(header):
    response = requests.get(BASE_URL+'/v1/user', headers=header)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"