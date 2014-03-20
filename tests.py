#!/usr/bin/env python3

# Initial setup code taken from Eric Wehrmeister
from urllib.request import urlopen
from urllib.request import Request
from json import dumps
import json

def test_list_players():
    pass

def test_create_player():
    pass

def test_get_player():
    pass

def test_modify_player():
    pass

def test_delete_player():
    pass

def test_list_playerYears():
    pass

def test_create_playerYear():
    pass

def test_get_playerYear():
    pass

def test_modify_playerYear():
    pass

def test_delete_playerYears():
    pass

def test_list_teams():
    pass

def test_create_team():
    pass

def test_get_team():
    pass

def test_modify_team():
    pass

def test_delete_team():
    pass

def test_list_teamYears():
    pass

def test_create_teamYear():
    pass

def test_get_teamYear():
    pass

def test_modify_teamYear():
    pass

def test_delete_teamYear():
    pass

def test_list_years():
    pass

def test_create_year():
    pass

def test_get_year():
    pass

def test_modify_year():
    pass

def test_delete_year():
    pass


def test_post():

    values = dumps({ "title": "Buy cheese and bread for breakfast." })
    headers = {"Content-Type": "application/json"}

    vbin = values.encode("utf-8") 

    request = Request("http://ccoleman812.apiary.io/notes", data=vbin, headers=headers)
    response = urlopen(request).readall().decode('utf-8')

    data = json.loads(response)

    print(data)

test_post()
