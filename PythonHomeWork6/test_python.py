import math
import pytest

def test_filter():
    mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'мак']
    mak = list(filter(lambda x: x == 'мак', mixed))
    proso = list(filter(lambda x: x == 'просо', mixed))
    assert proso == ['просо', 'просо', 'просо', 'просо']


def test_map():
    l1 = [1,2,3]
    l2 = [4,5,6] 
    map_list = list(map(lambda x,y: x + y, l1, l2))
    assert map_list == [5, 7, 9] 

    mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
    kilometer_distances = list(map(lambda num_miles: num_miles * 1.6, mile_distances))
    assert kilometer_distances == [1.6, 10.4, 27.84, 3.84, 14.4]

def test_sorted():
    s2="hello"
    assert sorted(s2) == ['e', 'h', 'l', 'l', 'o']
    l1=[1, 4, 5, 2, 456, 12]
    assert sorted(l1) == [1, 2, 4, 5, 12, 456]
    assert sorted(l1, reverse=True) == [456, 12, 5, 4, 2, 1]

def test_pi(): 
    assert math.pi == 3.141592653589793

def test_sqrt():
    assert math.sqrt(625) == 25
    assert math.sqrt(256) == 16

def test_pow(): 
    assert math.pow(5,4) == 625
    assert math.pow(2, 10) == 1024

def test_hypot(): 
    assert math.hypot(3, 4) == 5

