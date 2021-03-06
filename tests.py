#!/usr/bin/env python3
from django.test import TestCase

import requests
#from urllib.request import Request
#from urllib.request import HTTPError
#from urllib.parse import urlencode
from json import dumps
import re
import json
import logging
import unittest
from copy import deepcopy
from idb.models import *

# ----------------
# Unit Tests - IDB
# ----------------

player = { 
      "name": "A Guy", 
      "number": 10, 
      "position": "OF",  
      "social": "@Bharper3407",
      "bats": "R", 
      "throws": "L", 
      "height": 74, 
      "weight": 230, 
      "school": "College of Southern Nevada"
    }
team = { 
          "abbr": "ZZZ", 
          "name": "A Team", 
          "social": "@Cardinals", 
          "city": "St. Louis", 
          "state": "MO", 
          "park": "Busch Stadium III", 
          "div": "NL Central", 
          "mgr": "Mike Matheny"
       } 
year = { "year": "2050", 
          "champion": "hello", 
          "AL_MVP": "Migdf asCabrera", 
          "NL_MVP": "Ddfsdf McCutchen", 
          "AL_CY": "Max Scherzer", 
          "NL_CY": "Clayton Kershaw"
        }
player_year = {
          "year": "2004", #year["year"], 
          "team": "Washington Nationals", #team["name"], 
          "kind": "hitter", 
          "games": 1, 
          "pa": 111, 
          "avg": 0.111, 
          "obp": 0.111, 
          "slg": 0.111, 
          "hr": 1, 
          "rbi": 1 
        }
team_year = { 
              "year": year["year"], 
              "wins": 11, 
              "losses": 11, 
              "standing": 1, 
              "playoffs": "Lost WS (4-2)", 
              "attend": 111111, 
              "payroll": 111111 
              }

url_main = "http://frozen-plateau-5382.herokuapp.com/api"

class TestIDB(TestCase):
  
    def test_player(self):
        headers = {"Content-Type": "application/json"}  
        """
            POST
        """
        data = json.dumps(player)
        data = data.encode('utf-8')
        response = requests.post(url_main + "/players/", data=data)
        data = response.json()
        p_id = data[0]["pk"]
        self.assertTrue(response.status_code == 201)
        #self.assertTrue(len(data) == 1) #TODO this is going to be false until we have our own json serializer
        #self.assertTrue(data == expected)
        self.assertDictEqual(player, data[0]["fields"])
        """
            GET
        """
        response = requests.get(url_main + "/players/" + str(p_id))
        data = response.json()
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(data) == 1)
        #self.check_data(data)
 
        """
           PUT
        """
        
        data = {"name" : "The Guy"}
        data = json.dumps(data)
        data = data.encode('utf-8')
        response = requests.put(url_main + "/players/" + str(p_id) + "/", data=data)
        data = response.json()
        self.assertTrue(response.status_code == 200)
        _player = deepcopy(player)
        _player["name"] = "The Guy"
        self.assertTrue(data[0]["fields"]["name"] == "The Guy")
        self.assertDictEqual(data[0]["fields"], _player)
        
        """
           DELETE
        """    
        
        response = requests.delete(url_main + "/players/" + str(p_id) + "/")
        self.assertTrue(response.status_code == 204)
        
        
    def test_team(self):
        headers = {"Content-Type": "application/json"}  
        """"
            POST
        """
        data = json.dumps(team)
        data = data.encode('utf-8')
        response = requests.post(url_main + "/teams/", data=data)
        data = response.json()
        t_id = data[0]["pk"]      
        self.assertTrue(response.status_code == 201)
        self.assertDictEqual(data[0]["fields"],team)
        """
           GET
        """
        response = requests.get(url_main + "/teams/" + str(t_id))
        data = response.json()
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(data) == 1)
        #self.check_data(data)

        """
            PUT
        """
        
        data = {"city": "Test City"}
        data = json.dumps(data)
        data = data.encode('utf-8')
        response = requests.put(url_main + "/teams/" + str(t_id) + "/", data=data)
        data = response.json()
        self.assertTrue(response.status_code == 200)
        _team = deepcopy(team)
        _team["city"] = "Test City"
        self.assertTrue(data[0]["fields"]["city"] == "Test City")
        self.assertDictEqual(data[0]["fields"], _team)
        
        
        """
           DELETE
        """
        
        response = requests.delete(url_main + "/teams/" + str(t_id) + "/")
        self.assertTrue(response.status_code == 204)
        
        
        
    def test_year(self):
        headers = {"Content-Type": "application/json"}
        """
           POST
        """
        data = json.dumps(year)
        data = data.encode('utf-8')
        response = requests.post(url_main + "/years/", data=data)
        data = response.json()
        self.assertTrue(response.status_code == 201)
        y_id = data[0]["pk"]
        self.assertDictEqual(year, data[0]["fields"])

        """
           GET
        """
        response = requests.get(url_main + "/years/" + str(y_id))
        data = response.json()
        
        self.assertTrue(response.status_code == 200)
        self.assertDictEqual(year, data[0]["fields"])
   
        """
           PUT
        """
        data = {"champion": "me"}
        data = json.dumps(data)
        data = data.encode('utf-8')
        response = requests.put(url_main + "/years/" + str(y_id) + "/", data=data)
        data = response.json()

        self.assertTrue(response.status_code == 200)
        self.assertTrue(data[0]["fields"]["champion"] == "me")
        _year = deepcopy(year)
        _year["champion"] = "me"
        self.assertDictEqual(_year, data[0]["fields"])
        
    
        """
           DELETE
        """
        headers = {"Content-Type": "application/json"}
        response = requests.delete(url_main + "/years/" + str(y_id) + "/")
        self.assertTrue(response.status_code == 204)
        
    
    # Float fields are causing issues
    def test_playerYear(self):
        headers = {"Content-Type": "application/json"}       
        """
            POST
        """
        # Create a Year
        data = json.dumps(year)
        data = data.encode('utf-8')
        response = requests.post(url_main + "/years/", data=data)
        data = response.json()
        self.assertTrue(response.status_code == 201)
        y_id = data[0]["pk"]
        # Create a Team
        data = json.dumps(team)
        data = data.encode('utf-8')
        response = requests.post(url_main + "/teams/", data=data)
        data = response.json()
        t_id = data[0]["pk"]      
        # Create a Player
        data = json.dumps(player)
        data = data.encode('utf-8')
        response = requests.post(url_main + "/players/", data=data)
        data = response.json()
        p_id = data[0]["pk"]
        # Create a Team Year
        data = json.dumps(team_year)
        data = data.encode('utf-8')
        response = requests.post(url_main + "/teams/" + str(t_id) + "/years", data=data)
        data = response.json()
        # Create a Player_Year
        data = json.dumps(player_year)
        data = data.encode('utf-8')
        response = requests.post(url_main + "/players/" + str(p_id) + "/years", data=data)
        data = response.json()
        self.assertTrue(response.status_code == 201)

        py_id = data[0]["pk"]

        """
           GET
        """    
        response = requests.get(url_main + "/players/" + str(p_id) + "/years/" + "2004")
        data = response.json()
        self.assertTrue(response.status_code == 200)
        #self.assertTrue(len(data) == 12)
        #self.assertTrue(data == expected)

        """
           PUT
        """  
        
        data = {"hr" : 2}
        data = json.dumps(data)
        data = data.encode('utf-8')
        response = requests.put(url_main + "/players/" + str(p_id) + "/years/2004", data=data)
        data = response.json()

        self.assertTrue(response.status_code == 200)
        
        """
           DELETE
        """
        response = requests.delete(url_main + "/players/" + str(p_id) + "/years/" + "2004")
        self.assertTrue(response.status_code == 204)
        
        # CleanUp
        response = requests.delete(url_main + "/teams/" + str(t_id) + "/years/" + "2004")
        response = requests.delete(url_main + "/years/" + str(y_id) + "/")
        response = requests.delete(url_main + "/teams/" + str(t_id) + "/")
        response = requests.delete(url_main + "/players/" + str(p_id) + "/")
        
    def test_teamYear(self):
        headers = {"Content-Type": "application/json"}  
        """
            POST
        """
        # Create a Team
        data = json.dumps(team)
        data = data.encode('utf-8')
        response = requests.post(url_main + "/teams/", data=data)
        data = response.json()
        t_id = data[0]["pk"]      
        # Create a Year
        data = json.dumps(year)
        data = data.encode('utf-8')
        response = requests.post(url_main + "/years/", data=data)
        data = response.json()
        self.assertTrue(response.status_code == 201)
        y_id = data[0]["pk"]  
        # Create a Team_Year
        data = json.dumps(team_year)
        data = data.encode('utf-8')
        response = requests.post(url_main + "/teams/" + str(t_id) + "/years", data=data)
        data = response.json()
        self.assertTrue(response.status_code == 201)
        _team_year = deepcopy(team_year)
        _team_year.pop("year", None)
        _team_year.pop("team", None)
        data[0]["fields"].pop("team", None)
        data[0]["fields"].pop("year", None)
        self.assertDictEqual(_team_year, data[0]["fields"])

        """
            GET
        """
        response = requests.get(url_main + "/teams/" + str(t_id) + "/years/" + str(y_id))
        data = response.json()

        self.assertTrue(response.status_code == 200)
        _team_year = deepcopy(team_year)
        _team_year.pop("year", None)
        _team_year.pop("team", None)
        data[0]["fields"].pop("team", None)
        data[0]["fields"].pop("year", None)
        self.assertDictEqual(_team_year, data[0]["fields"])
   
        """
           PUT
        """
        data = {"wins": "11"}
        data = json.dumps(data)
        data = data.encode('utf-8')
        response = requests.put(url_main + "/teams/" + str(t_id) + "/years/" + str(y_id), data=data)
        data = response.json()
        self.assertTrue(response.status_code == 200)
        _team_year = deepcopy(team_year)
        _team_year.pop("year", None)
        _team_year.pop("team", None)
        _team_year["wins"] = "11"
        data[0]["fields"].pop("team", None)
        data[0]["fields"].pop("year", None)
        self.assertDictEqual(_team_year, data[0]["fields"])
    
        """
           DELETE
        """    
        response = requests.delete(url_main + "/teams/" + str(t_id) + "/years/" + str(y_id))
        self.assertTrue(response.status_code == 204)
        
        # clean up
        response = requests.delete(url_main + "/years/" + str(y_id) + "/")
        response = requests.delete(url_main + "/teams/" + str(t_id) + "/")
    # -----------------
    # Test Player Group
    # -----------------
    """
    Tests the GET functionality for api/players/
    """
    def test_list_players(self):
      
        headers = {"Content-Type": "application/json"}
        response = requests.get(url_main + "/players/")
        data = response.json()
        self.assertTrue(response.status_code == 200)

    # ----------------------
    # Test Player Year Group
    # ----------------------

    
    # @unittest.skip("Don't mess with shit.")
    def test_list_playerYears(self):
        headers = {"Content-Type": "application/json"}
    
        response = requests.get(url_main + "/players/1/years")
        data = response.json()
        
        #print("List PlayerYears: " + str(data))

        self.assertTrue(response.status_code == 200)
        #self.assertTrue(len(data) == 2)
        #self.assertTrue(len(data[0]) == len(data[1]))
    
    
    
    
    # ----------------
    # Test Team Group
    # ----------------

    """
    Tests the GET functionality of api/teams/
    """
    def test_list_teams(self):
        headers = {"Content-Type": "application/json"}
    
        response = requests.get(url_main + "/teams/")
        data = response.json()
        self.assertTrue(response.status_code == 200)
    
    # -------------------
    # Test Team Year Group
    # --------------------

    def test_list_teamYears(self):
        headers = {"Content-Type": "application/json"}
    
        response = requests.get(url_main + "/teams/1/years")
        data = response.json()
        self.assertTrue(response.status_code == 200)
    
    # ---------------
    # Test Year Group
    # ---------------

    """
    Tests the GET functionality of api/years/
    """
    def test_list_years(self):
        headers = {"Content-Type": "application/json"}
        response = requests.get(url_main + "/years/")
        data = response.json()
        self.assertTrue(response.status_code == 200)
    
    
    """
    Data tester
    @param data in JSON format
    """
    def check_data(self, data):
        for entry in data:
            if entry["model"] == "idb.player":
                self.check_player_data(entry["fields"])
            elif entry["model"] == "idb.team":
                self.check_team_data(entry["fields"])
            elif entry["model"] == "idb.year":
                self.check_year_data(entry["fields"])
            elif entry["model"] == "idb.year":
                self.check_year_data(entry["fields"])
            else:
                print("Y'got problems.")

    """
    Generic player data tester
    @param JSON-formatted fields in our player model with corresponding values
    """
    def check_player_data(self, data):
        self.assertTrue(len(data) == 9)
        self.assertEqual(data.keys(), {"name", "position", "school", "throws", "social", "number", "bats", "height", "weight"})
        self.assertIn(data["position"], {"OF", "P", "1B", "SS"})
        self.assertIn(data["throws"], {"R", "L"})
        self.assertIn(data["bats"], {"R", "L"})
        self.assertTrue(self.check_name(data["name"]))
        self.assertTrue(self.check_twit(data["social"]))
        self.assertTrue(self.check_num(data["number"]))
        self.assertTrue(self.check_num(data["height"]))
        self.assertTrue(self.check_num(data["weight"]))

    """
    Generic team data tester
    @param JSON-formatted fields in our team model with corresponding values
    """
    def check_team_data(self, data):
        self.assertTrue(len(data) == 8)
        self.assertEqual(data.keys(), {"name", "park", "city", "div", "social", "abbr", "state", "mgr"})
        self.assertIn(data["div"], {"AL Central", "AL West", "AL East", "NL Central", "NL West", "NL East"})
        self.assertTrue(self.check_twit(data["social"]))
        self.assertTrue(self.check_name(data["mgr"]))
        self.assertTrue(re.match("[A-Z][A-Z][A-Z]", data["abbr"]) is not None)
        self.assertTrue(re.match("[A-Z][A-Z]", data["state"]) is not None)

    """
    Generic year data tester
    @param JSON-formatted fields in our year model with corresponding values
    """
    def check_year_data(self, data):
        self.assertTrue(len(data) == 6)
        self.assertEqual(data.keys(), {"AL_CY", "champion", "AL_MVP", "NL_CY", "NL_MVP", "year"})
        self.assertTrue(self.check_name(data["AL_CY"]))
        self.assertTrue(self.check_name(data["AL_MVP"]))
        self.assertTrue(self.check_name(data["NL_CY"]))
        self.assertTrue(self.check_name(data["NL_MVP"]))

    """
    Simplistic check for name formatting.
    @param name to check
    @return True if name is two strings with proper capitalization separated by a space.
    """
    def check_name(self, name):
        # Note: Does silly things to allow for first names like CC and last name like Mc*
        return (re.match("^[A-Z]+[a-z]* [A-Z][a-z]+[A-Z]?[a-z]*$", str(name)) is not None)

    """
    Simplistic check for valid Twitter handle
    @param handle to check
    @return True if handle is empty OR a string beginning with @ followed by 
            one or more simple characters. Else, False.
    """
    def check_twit(self, handle):
        return (len(handle) == 0 or re.match("^@[A-Za-z0-9]+$", str(handle)) is not None)


    """
    Check to see if the given parameter is numeric.
    @param number to check
    @return True if numeric, else False.
    """
    def check_num(self, num):
        return (re.match("[0-9]*", str(num)) is not None)


