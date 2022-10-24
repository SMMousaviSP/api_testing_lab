import pytest
import requests
from local_config import TOKEN

BASE_URL = "https://api.gitter.im"

@pytest.fixture
def header():
    return {'Authorization': 'Bearer ' + TOKEN}

@pytest.fixture
def id_room(header):
    return requests.get(BASE_URL+'/v1/rooms', headers=header).json()[0]['id']

@pytest.fixture
def id_personal_room(header):
    return requests.get(BASE_URL+'/v1/rooms', headers=header).json()[1]['id']


@pytest.fixture
def id_first_message(header, id_room):
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room+'/chatMessages', headers=header)
    return response.json()[0]['id']

@pytest.mark.status_code
def test_all_messages_header(header, id_room):
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room+'/chatMessages', headers=header)
    assert response.status_code==200


def test_messages_count(header,id_room): # not a good example
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room+'/chatMessages', headers=header)
    assert len(response.json()) > 0

def test_messages_count_limit(header,id_room): # not a good example
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room+'/chatMessages?limit=1', headers=header)
    assert len(response.json()) < 2

def test_message_get_first_sender(header, id_room):
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room+'/chatMessages', headers=header)
    assert response.json()[0]['fromUser']['username']=="SMMousaviSP"

@pytest.mark.parametrize("index, sender", [(0,"SMMousaviSP"), (1,"celiafritsch")])
def test_message_check_multiple_senders(header,id_room, index, sender):
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room+'/chatMessages', headers=header)
    assert response.json()[index]['fromUser']['username']==sender



#specific message
def test_get_sender(header, id_room, id_first_message):
    response = requests.get(BASE_URL+'/v1/rooms/'+id_room+'/chatMessages/'+id_first_message, headers=header)
    assert response.json()['fromUser']['username']=="SMMousaviSP"


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
def test_update_message_another_sender(header, id_room,id_first_message):
    body_updated={"text":"ciao !"}
    response = requests.put(BASE_URL+'/v1/rooms/'+id_room+'/chatMessages/'+id_first_message, data=body_updated ,headers=header)
    assert response.status_code==403 #forbidden

@pytest.mark.status_code
def test_send_and_delete_message(header,id_personal_room):
    body = {"text":"temporary message"}
    response = requests.post(BASE_URL+'/v1/rooms/'+id_personal_room+'/chatMessages/', data=body, headers=header)
    assert response.status_code==200
    id_message = response.json()['id']
    response2 = requests.delete(BASE_URL+'/v1/rooms/'+id_personal_room+'/chatMessages/'+id_message, headers=header)
    assert response2.status_code==204

