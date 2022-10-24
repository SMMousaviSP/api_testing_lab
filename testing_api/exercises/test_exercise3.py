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



#def test_send_and_update_message():
    # complete this part

#def test_send_and_delete_message():