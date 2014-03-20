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
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 2)
        self.assertTrue(len(data[0]) == len(data[1]))
        self.assertTrue(len(data[0]) == 12)
    
    def test_create_player(self):
        headers = {"Content-Type": "application/json"}
        values = dumps({ "bats": "R" })
        vbin = values.encode("utf-8") 
    
        request = Request("http://mlbapi.apiary-mock.com/api/players", data=vbin, headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))

        self.assertTrue(request.get_method() == "POST")
        self.assertTrue(response.getcode() == 201)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data["name"] == "Bryce Harper")

    def test_get_player(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data["name"] == "Bryce Harper")
        self.assertTrue(data["position"] == "OF")
   
    def test_modify_player(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1", headers=headers)
        request.get_method = lambda: 'PUT' # StackOverflow hack :/
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))

        self.assertTrue(request.get_method() == "PUT") # bit superfluous
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data["name"] == "Bryce Harper")
        self.assertTrue(data["position"] == "1B")
    
    def test_delete_player(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1", headers=headers)
        request.get_method = lambda: 'DELETE' # StackOverflow hack :/
        response = urlopen(request)

        self.assertTrue(response.getcode() == 204)
        self.assertTrue(request.get_method() == "DELETE") # bit superfluous
    
    def test_list_playerYears(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1/years", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 2)
        self.assertTrue(len(data[0]) == len(data[1]))
        self.assertTrue(len(data[0]) == 12)
        self.assertTrue(data[0]["hr"] == "22")
    
    def test_create_playerYear(self):
        headers = {"Content-Type": "application/json"}
        values = dumps({ "bats": "R" }) # dummy
        vbin = values.encode("utf-8") 
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1/years", data=vbin, headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))

        self.assertTrue(request.get_method() == "POST")
        self.assertTrue(response.getcode() == 201)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data["year"] == "2012")
        self.assertTrue(data["pa"] == "597")

    def test_get_playerYear(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1/years/1", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data["year"] == "2012")
        self.assertTrue(data["hr"] == "22")
   
    def test_modify_playerYear(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1/years/1", headers=headers)
        request.get_method = lambda: 'PUT' 
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))

        self.assertTrue(request.get_method() == "PUT") # bit superfluous
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data["team"] == "TEX")
    
    def test_delete_playerYears(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1/years/1", headers=headers)
        request.get_method = lambda: 'DELETE' 
        response = urlopen(request)

        self.assertTrue(response.getcode() == 204)
        self.assertTrue(request.get_method() == "DELETE") # bit superfluous
    
    def test_list_teams(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 2)
        self.assertTrue(len(data[0]) == len(data[1]))
        self.assertTrue(len(data[0]) == 11)
        self.assertTrue(data[0]["abbr"] == "LAA")
    
    def test_create_team(self):
        headers = {"Content-Type": "application/json"}
        values = dumps({ "bats": "R" }) # dummy
        vbin = values.encode("utf-8") 
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams", data=vbin, headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))

        self.assertTrue(request.get_method() == "POST")
        self.assertTrue(response.getcode() == 201)
        self.assertTrue(len(data) == 11)
        self.assertTrue(data["abbr"] == "LAD")
    
    def test_get_team(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams/1", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 11)
        self.assertTrue(data["id"] == "1")
        self.assertTrue(data["abbr"] == "LAA")
    
    def test_modify_team(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams/1", headers=headers)
        request.get_method = lambda: 'PUT' 
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        
        self.assertTrue(request.get_method() == "PUT") # bit superfluous
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 11)
        self.assertTrue(data["social"] == "@LA_Angels")
    
    def test_delete_team(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams/1", headers=headers)
        request.get_method = lambda: 'DELETE' # StackOverflow hack :/
        response = urlopen(request)

        self.assertTrue(response.getcode() == 204)
        self.assertTrue(request.get_method() == "DELETE") # bit superfluous
    
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

unittest.main()
