import requests
import pytest

from local_config import TOKEN

BASE_URL = "https://api.gitter.im"


def test_user_header():
    header = {'Authorization': 'Bearer ' + TOKEN}
    response = requests.get(BASE_URL+'/v1/user', headers=header)
    assert response.status_code==200

def test_get_check_content_type():
    header = {'Authorization': 'Bearer ' + TOKEN}
    response = requests.get(BASE_URL+'/v1/user', headers=header)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


# def test_user_username():
#     header = {'Authorization': 'Bearer ' + TOKEN}
#     response = requests.get(BASE_URL+'/v1/user', headers=header)
#     # assert response.json()[0]['displayName']== #complete with your name


# def test_user_username():
#     header = {'Authorization': 'Bearer ' + TOKEN}
#     response = requests.get(BASE_URL+'/v1/user', headers=header)
#     # Write an assert that checks if the displayName is a string (str in python)
#     # To get the type of a variable : type(name_variable) 

