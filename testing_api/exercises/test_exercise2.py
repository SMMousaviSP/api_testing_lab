import requests
import pytest

from local_config import TOKEN

BASE_URL = "https://api.gitter.im"

@pytest.fixture
def header():
    return {'Authorization': 'Bearer ' + TOKEN}


# 2. create a new fixture for getting the id_room of the first room. This fixture could replace the first line of the function test_check_type_counter

# 1. Complete with the call to the API 
# def test_check_type_counter(header):
#     id_room = requests.get(BASE_URL+'/v1/rooms', headers=header).json()[0]['id']
#     # call the API for obtaining the information about this room
#     assert type(response.json()['userCount'])==int


#3. complete this function with the fixture that returns the header, the id_room and with the call to the API
# def test_get_security():
#     assert response.json()['security']=="PUBLIC" # change here if the security of your room is not public
