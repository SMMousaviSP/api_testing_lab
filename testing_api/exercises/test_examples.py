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



# Uncomment the code for testing

# def test_get_first_element():
#     liste = [2,3,5,8]
#     #Write here the missing part for writing a test for the function get_first_element

# def test_get_first_element_empty_list():
#     liste = []
#     #Write here the missing part for writing a test for the function get_first_element

