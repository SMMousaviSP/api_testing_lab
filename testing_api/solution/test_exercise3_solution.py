import pytest
import requests
from local_config import TOKEN

BASE_URL = "https://api.gitter.im"

@pytest.fixture
def header():
    return {'Authorization': 'Bearer ' + TOKEN}


@pytest.fixture
def id_personal_room(header):
    return requests.get(BASE_URL+'/v1/rooms', headers=header).json()[1]['id']


@pytest.mark.skip
def test_send_message(header, id_personal_room):
    body = {"text":"message sent with python"}
    response = requests.post(BASE_URL+'/v1/rooms/'+id_personal_room+'/chatMessages/', data=body, headers=header)
    assert response.status_code==200
    assert response.json()["text"]=="message sent with python"

@pytest.mark.skip
def test_send_and_update_message(header, id_personal_room):
    body = {"text":"first version of the message"}
    response = requests.post(BASE_URL+'/v1/rooms/'+id_personal_room+'/chatMessages/', data=body, headers=header)
    assert response.status_code==200
    id_message = response.json()['id']
    body_updated = {"text":"message updated"}
    response2 = requests.put(BASE_URL+'/v1/rooms/'+id_personal_room+'/chatMessages/'+id_message, data=body_updated, headers=header)
    assert response2.status_code==200
    assert response.json()["text"]=="first version of the message"
    assert response2.json()["text"]=="message updated"


@pytest.mark.status_code
def test_send_and_delete_message(header,id_personal_room):
    body = {"text":"temporary message"}
    response = requests.post(BASE_URL+'/v1/rooms/'+id_personal_room+'/chatMessages/', data=body, headers=header)
    assert response.status_code==200
    id_message = response.json()['id']
    response2 = requests.delete(BASE_URL+'/v1/rooms/'+id_personal_room+'/chatMessages/'+id_message, headers=header)
    assert response2.status_code==204