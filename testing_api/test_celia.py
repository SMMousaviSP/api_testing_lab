import requests
import pytest

from local_config import TOKEN

BASE_URL = "https://api.gitter.im"


@pytest.fixture
def header():
    return {'Authorization': 'Bearer ' + TOKEN}

@pytest.fixture
def id_room(header):
    return requests.get(BASE_URL+'/v1/rooms', headers=header).json()[0]['id']


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



def test_get_first_user_room(header, id_room):
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room+'/users', headers=header)
    assert response.json()[0]['displayName']=="SMMousaviSP"


def test_get_count_users(header,id_room): # not a good example
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room, headers=header)
    assert response.json()['userCount']==2


def test_check_type_counter(header,id_room):
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room, headers=header)
    assert type(response.json()['userCount'])==int

def test_get_security(header,id_room):
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room, headers=header)
    assert response.json()['security']=="PUBLIC"



def test_permission_admin_right(header,id_room):
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room, headers=header)
    assert response.json()['permissions']['admin'] == False

def test_permission_admin_type(header,id_room):
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room, headers=header)
    assert type(response.json()['permissions']['admin'])==bool



