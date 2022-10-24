import pytest

def sum(a,b):
    return a+b

def test_sum():
    assert sum(2,3)==5




def get_first_element(liste):
    if (len(liste)>0):
        return liste[0]
    else :
        return -1


def test_get_first_element():
    liste = [2,3,5,8]
    assert get_first_element(liste)==2

def test_get_first_element_empty_list():
    liste = []
    assert get_first_element(liste)==-1
