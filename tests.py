#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.request import Request
from json import dumps
import json
import unittest

# ----------------
# Unit Tests - IDB
# ----------------

class TestIDB(unittest.TestCase):

    def test_list_players(self):
        pass
    
    def test_create_player(self):
        pass
    
    def test_get_player(self):
        pass
    
    def test_modify_player(self):
        pass
    
    def test_delete_player(self):
        pass
    
    def test_list_playerYears(self):
        pass
    
    def test_create_playerYear(self):
        pass
    
    def test_get_playerYear(self):
        pass
    
    def test_modify_playerYear(self):
        pass
    
    def test_delete_playerYears(self):
        pass
    
    def test_list_teams(self):
        pass
    
    def test_create_team(self):
        pass
    
    def test_get_team(self):
        pass
    
    def test_modify_team(self):
        pass
    
    def test_delete_team(self):
        pass
    
    def test_list_teamYears(self):
        pass
    
    def test_create_teamYear(self):
        pass
    
    def test_get_teamYear(self):
        pass
    
    def test_modify_teamYear(self):
        pass
    
    def test_delete_teamYear(self):
        pass
    
    def test_list_years(self):
        pass
    
    def test_create_year(self):
        pass
    
    def test_get_year(self):
        pass
    
    def test_modify_year(self):
        pass
    
    def test_delete_year(self):
        pass
    
    # Initial setup code taken from Eric Wehrmeister, Piazza
    def test_post(self):
    
        values = dumps({ "title": "Buy cheese and bread for breakfast." })
        headers = {"Content-Type": "application/json"}
    
        vbin = values.encode("utf-8") 
    
        request = Request("http://ccoleman812.apiary.io/notes", data=vbin, headers=headers)
        response = urlopen(request).readall().decode('utf-8')
    
        data = json.loads(response)
    
        #print(data)
        self.assertTrue(True)

# ----
# main
# ----

print("Start IDB testing...")
unittest.main()
print("Done.")
