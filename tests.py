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

    # -----------------
    # Test Player Group
    # -----------------

    def test_list_players(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = [
            {
                "id": "1",
                "name": "Bryce Harper",
                "social": "@Bharper3407",
                "position": "OF",
                "number": "34",
                "bats": "L",
                "throws": "L",
                "height": "74",
                "weight": "230",
                "school": "College of Southern Nevada",
                "years": ["2012", "2013"],
                "images": ["http://mlb.com/images/players/525x330/547180.jpg"]
            }, {
                "id": "2",
                "name": "Mike Trout",
                "social": "@Trouty20",
                "position": "OF",
                "number": "27",
                "bats": "R",
                "throws": "R",
                "height": "74",
                "weight": "230",
                "school": "Millville Senior HS",
                "years": ["2011", "2012", "2013"],
                "images": ["http://mlb.com/images/players/525x330/545361.jpg"]
            }
        ]
        

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 2)
        self.assertTrue(len(data[0]) == len(data[1]))
        self.assertTrue(len(data[0]) == 12)
        self.assertTrue(data == expected)
    
    def test_create_player(self):
        headers = {"Content-Type": "application/json"}
        values = dumps({ "bats": "R" })
        vbin = values.encode("utf-8") 
    
        request = Request("http://mlbapi.apiary-mock.com/api/players", data=vbin, headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "3",
            "name": "Bryce Harper",
            "social": "@Bharper3407",
            "position": "OF",
            "number": "34",
            "bats": "L",
            "throws": "L",
            "height": "74",
            "weight": "230",
            "school": "College of Southern Nevada",
            "years": ["2012", "2013"],
            "images": ["http://mlb.com/images/players/525x330/547180.jpg"]    
        }

        self.assertTrue(request.get_method() == "POST")
        self.assertTrue(response.getcode() == 201)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data["name"] == "Bryce Harper")
        self.assertTrue(data == expected)

    def test_get_player(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "3",
            "name": "Bryce Harper",
            "social": "@Bharper3407",
            "position": "OF",
            "number": "34",
            "bats": "L",
            "throws": "L",
            "height": "74",
            "weight": "230",
            "school": "College of Southern Nevada",
            "years": ["2012", "2013"],
            "images": ["http://mlb.com/images/players/525x330/547180.jpg"]
        }

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data["name"] == "Bryce Harper")
        self.assertTrue(data["position"] == "OF")
        self.assertTrue(data == expected)
   
    def test_modify_player(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1", headers=headers)
        request.get_method = lambda: 'PUT' # StackOverflow hack :/
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "3",
            "name": "Bryce Harper",
            "social": "@Bharper3407",
            "position": "1B",
            "number": "34",
            "bats": "L",
            "throws": "L",
            "height": "74",
            "weight": "230",
            "school": "College of Southern Nevada",
            "years": ["2012", "2013"],
            "images": ["http://mlb.com/images/players/525x330/547180.jpg"]  
        }

        self.assertTrue(request.get_method() == "PUT") # bit superfluous
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data["name"] == "Bryce Harper")
        self.assertTrue(data["position"] == "1B")
        self.assertTrue(data == expected)
    
    def test_delete_player(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1", headers=headers)
        request.get_method = lambda: 'DELETE' # StackOverflow hack :/
        response = urlopen(request)

        self.assertTrue(response.getcode() == 204)
        self.assertTrue(request.get_method() == "DELETE") # bit superfluous
    
    # ----------------------
    # Test Player Year Group
    # ----------------------

    def test_list_playerYears(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1/years", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = [
            {
                "id": "1",
                "year": "2012",
                "team": "WSN",
                "type": "hitter",
                "games": "139",
                "pa": "597",
                "avg": ".270",
                "obp": ".340",
                "slg": ".477",
                "hr": "22",
                "rbi": "59",
                "player_id": "1"
            }, {
                "id": "2",
                "year": "2013",            
                "team": "WSN",
                "type": "hitter",
                "games": "118",
                "pa": "497",
                "avg": ".274",
                "obp": ".368",
                "slg": ".486",
                "hr": "20",
                "rbi": "58",
                "player_id": "1"
            }
        ]

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 2)
        self.assertTrue(len(data[0]) == len(data[1]))
        self.assertTrue(len(data[0]) == 12)
        self.assertTrue(data[0]["hr"] == "22")
        self.assertTrue(data == expected)
    
    def test_create_playerYear(self):
        headers = {"Content-Type": "application/json"}
        values = dumps({ "bats": "R" }) # dummy
        vbin = values.encode("utf-8") 
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1/years", data=vbin, headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "1", 
            "year": "2012",
            "team": "WSN",
            "type": "hitter",
            "games": "139",
            "pa": "597",
            "avg": ".270",
            "obp": ".340",
            "slg": ".477",
            "hr": "22",
            "rbi": "59",
            "player_id": "1"
        }

        self.assertTrue(request.get_method() == "POST")
        self.assertTrue(response.getcode() == 201)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data["year"] == "2012")
        self.assertTrue(data["pa"] == "597")
        self.assertTrue(data == expected)

    def test_get_playerYear(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1/years/1", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "1", 
            "year": "2012",
            "team": "WSN",
            "type": "hitter",
            "games": "139",
            "pa": "597",
            "avg": ".270",
            "obp": ".340",
            "slg": ".477",
            "hr": "22",
            "rbi": "59",
            "player_id": "1"
        }

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data == expected)
   
    def test_modify_playerYear(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1/years/1", headers=headers)
        request.get_method = lambda: 'PUT' 
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "1", 
            "year": "2012",
            "team": "TEX",
            "type": "hitter",
            "games": "139",
            "pa": "597",
            "avg": ".270",
            "obp": ".340",
            "slg": ".477",
            "hr": "22",
            "rbi": "59",
            "player_id": "1"
        }

        self.assertTrue(request.get_method() == "PUT") # bit superfluous
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 12)
        self.assertTrue(data == expected)
    
    def test_delete_playerYears(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/players/1/years/1", headers=headers)
        request.get_method = lambda: 'DELETE' 
        response = urlopen(request)

        self.assertTrue(response.getcode() == 204)
        self.assertTrue(request.get_method() == "DELETE") # bit superfluous
    
    # ----------------
    # Test Team Group
    # ----------------

    def test_list_teams(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = [
            {
                "id": "1",
                "name": "Los Angeles Angels of Anaheim",
                "abbr": "LAA",
                "city": "Los Angeles",
                "state": "CA",
                "park": "Angel Stadium of Anaheim",
                "div": "AL West",
                "social": "@Angels",
                "mgr": "Mike Scioscia",
                "years": ["2004","2005","2006","2007","2008","2009","2010","2011","2012", "2013"],
                "images": ["http://content.sportslogos.net/logos/53/922/thumbs/wsghhaxkh5qq0hdkbt1b5se41.gif"]
            }, {
                "id": "2",
                "name": "St. Louis Cardinals",
                "abbr": "STL",
                "city": "St. Louis",
                "state": "MO",
                "park": "Busch Stadium III",
                "div": "NL Central",
                "social": "@Cardinals",
                "mgr": "Mike Matheny",
                "years": ["2004","2005","2006","2007","2008","2009","2010","2011","2012", "2013"],
                "images": ["http://content.sportslogos.net/logos/54/72/thumbs/3zhma0aeq17tktge1huh7yok5.gif"]
            }
        ]

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 2)
        self.assertTrue(len(data[0]) == len(data[1]))
        self.assertTrue(len(data[0]) == 11)
        self.assertTrue(data == expected)
    
    def test_create_team(self):
        headers = {"Content-Type": "application/json"}
        values = dumps({ "bats": "R" }) # dummy
        vbin = values.encode("utf-8") 
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams", data=vbin, headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "3",
            "name": "Los Angeles Dodgers",
            "abbr": "LAD",
            "city": "Los Angeles",
            "state": "CA",
            "park": "Dodger Stadium",
            "div": "NL West",
            "social": "@Dodgers",
            "mgr": "Don Mattingly",
            "years": ["2004","2005","2006","2007","2008","2009","2010","2011","2012", "2013"],
            "images": ["http://content.sportslogos.net/logos/54/63/thumbs/efvfv5b5g1zgpsf56gb04lthx.gif"]
        }

        self.assertTrue(request.get_method() == "POST")
        self.assertTrue(response.getcode() == 201)
        self.assertTrue(len(data) == 11)
        self.assertTrue(data == expected)
    
    def test_get_team(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams/1", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "1",
            "name": "Los Angeles Angels of Anaheim",
            "abbr": "LAA",
            "city": "Los Angeles",
            "state": "CA",
            "park": "Angel Stadium of Anaheim",
            "div": "AL West",
            "social": "@Angels",
            "mgr": "Mike Scioscia",
            "years": ["2004","2005","2006","2007","2008","2009","2010","2011","2012", "2013"],
            "images": ["http://content.sportslogos.net/logos/54/72/thumbs/3zhma0aeq17tktge1huh7yok5.gif"]
        }

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 11)
        self.assertTrue(data == expected)
    
    def test_modify_team(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams/1", headers=headers)
        request.get_method = lambda: 'PUT' 
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "1",
            "name": "Los Angeles Angels of Anaheim",
            "abbr": "LAA",
            "city": "Los Angeles",
            "state": "CA",
            "park": "Angel Stadium of Anaheim",
            "div": "AL West",
            "social": "@LA_Angels",
            "mgr": "Mike Scioscia",
            "years": ["2004","2005","2006","2007","2008","2009","2010","2011","2012", "2013"],
            "images": ["http://content.sportslogos.net/logos/54/72/thumbs/3zhma0aeq17tktge1huh7yok5.gif"]
        }
        
        self.assertTrue(request.get_method() == "PUT") # bit superfluous
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 11)
        self.assertTrue(data == expected)
    
    def test_delete_team(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams/1", headers=headers)
        request.get_method = lambda: 'DELETE' # StackOverflow hack :/
        response = urlopen(request)

        self.assertTrue(response.getcode() == 204)
        self.assertTrue(request.get_method() == "DELETE") # bit superfluous

    # --------------------
    # Test Team Year Group
    # --------------------

    def test_list_teamYears(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams/1/years", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = [
            {
                "id": "1",
                "year": "2013",
                "wins": "78",
                "losses": "84",
                "standing": "4",
                "playoffs": "Lost LDS (3-2)",
                "attend": "3019505",
                "payroll": "$116032500",
                "team_id": "1"
            }, {
                "id": "2",
                "year": "2012",
                "wins": "89",
                "losses": "73",
                "standing": "3",
                "playoffs": "Lost LDS (3-2)",
                "attend": "3061770",
                "payroll": "$140581000",
                "team_id": "1"
            }
        ]

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 2)
        self.assertTrue(len(data[0]) == len(data[1]))
        self.assertTrue(len(data[0]) == 9)
        self.assertTrue(data == expected)
    
    def test_create_teamYear(self):
        headers = {"Content-Type": "application/json"}
        values = dumps({ "bats": "R" }) # dummy
        vbin = values.encode("utf-8") 
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams/1/years", data=vbin, headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "3",
            "year": "2011",
            "wins": "86",
            "losses": "76",
            "standing": "2",
            "playoffs": "Lost LDS (3-2)",
            "attend": "3166321",
            "payroll": "$138543166",
            "team_id": "1"
        }

        self.assertTrue(request.get_method() == "POST")
        self.assertTrue(response.getcode() == 201)
        self.assertTrue(len(data) == 9)
        self.assertTrue(data == expected)

    def test_get_teamYear(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams/1/years/1", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "1",
            "year": "2013",
            "wins": "78",
            "losses": "84",
            "standing": "4",
            "playoffs": "Lost LDS (3-2)",
            "attend": "3019505",
            "payroll": "$116032500",
            "team_id": "1"
        }

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 9)
        self.assertTrue(data == expected)
   
    def test_modify_teamYear(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams/1/years/1", headers=headers)
        request.get_method = lambda: 'PUT' 
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "1",
            "year": "2013",
            "wins": "78",
            "losses": "84",
            "standing": "4",
            "playoffs": "Lost LDS (3-2)",
            "attend": "3019505",
            "payroll": "$116032500",
            "team_id": "1"
        }

        self.assertTrue(request.get_method() == "PUT") # bit superfluous
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 9)
        self.assertTrue(data == expected)
    
    def test_delete_teamYears(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/teams/1/years/1", headers=headers)
        request.get_method = lambda: 'DELETE' 
        response = urlopen(request)

        self.assertTrue(response.getcode() == 204)
        self.assertTrue(request.get_method() == "DELETE") # bit superfluous
    
    # ---------------
    # Test Year Group
    # ---------------

    def test_list_years(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/years", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = [
            {
                "id": "2013",
                "champion": "Boston Red Sox",
                "standings": ["BOS", "STL", "OAK", "ATL", "PIT", "DET", "LAD", "CLE", "TBR", "TEX", "CIN", "WSN", "KCR", "NYY", "BAL", "ARI", "LAA", "SDP", "SFG", "NYM", "MIL", "TOR", "COL", "PHI", "SEA", "MIN", "CHC", "CHW", "MIA", "HOU"],
                "AL_MVP": "Cabrera",
                "NL_MVP": "McCutchen",
                "AL_CY": "Max Scherzer",
                "NL_CY": "Clayton Kershaw"
            }, {
                "id": "2012",
                "champion": "San Francisco Giants",
                "standings": ["WSN", "CIN", "NYY", "OAK", "SFG", "ATL", "BAL", "TEX", "TBR", "LAA", "DET", "STL", "LAD", "CHW", "MIL", "PHI", "ARI", "PIT", "SDP", "SEA", "NYM", "TOR", "KCR", "MIA", "BOS", "CLE", "MIN", "COL", "CHC", "HOU"],
                "AL_MVP": "Cabrera",
                "NL_MVP": "Buster Posey",
                "AL_CY": "David Price",
                "NL_CY": "RA Dickey"
            }
        ]

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 2)
        self.assertTrue(len(data[0]) == len(data[1]))
        self.assertTrue(len(data[0]) == 7)
        self.assertTrue(data == expected)
    
    def test_create_year(self):
        headers = {"Content-Type": "application/json"}
        values = dumps({ "bats": "R" }) # dummy
        vbin = values.encode("utf-8") 
    
        request = Request("http://mlbapi.apiary-mock.com/api/years", data=vbin, headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "2011",
            "champion": "St. Louis Cardinals",
            "standings": ["PHI", "NYY", "MIL", "TEX", "ARI", "DET", "TBR", "STL", "BOS", "ATL", "LAA", "SFG", "LAD", "TOR", "WSN", "CLE", "CHW", "CIN", "NYM", "OAK", "COL", "PIT", "FLA", "KCR", "SDP", "CHC", "BAL", "SEA", "MIN", "HOU"],
            "AL_MVP": "Justin Verlander",
            "NL_MVP": "Ryan Braun",
            "AL_CY": "Justin Verlander",
            "NL_CY": "Clayton Kershaw"
        }

        self.assertTrue(request.get_method() == "POST")
        self.assertTrue(response.getcode() == 201)
        self.assertTrue(len(data) == 7)
        self.assertTrue(data == expected)

    def test_get_year(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/years/1", headers=headers)
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "2013",
            "champion": "Boston Red Sox",
            "standings": ["BOS", "STL", "OAK", "ATL", "PIT", "DET", "LAD", "CLE", "TBR", "TEX", "CIN", "WSN", "KCR", "NYY", "BAL", "ARI", "LAA", "SDP", "SFG", "NYM", "MIL", "TOR", "COL", "PHI", "SEA", "MIN", "CHC", "CHW", "MIA", "HOU"],
            "AL_MVP": "Cabrera",
            "NL_MVP": "McCutchen",
            "AL_CY": "Max Scherzer",
            "NL_CY": "Clayton Kershaw"
        }

        self.assertTrue(request.get_method() == "GET")
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 7)
        self.assertTrue(data == expected)
   
    def test_modify_year(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/years/1", headers=headers)
        request.get_method = lambda: 'PUT' 
        response = urlopen(request)
        data = json.loads(response.readall().decode('utf-8'))
        expected = {
            "id": "2013",
            "champion": "Boston Red Sox",
            "standings": ["BOS", "STL", "OAK", "ATL", "PIT", "DET", "LAD", "CLE", "TBR", "TEX", "CIN", "WSN", "KCR", "NYY", "BAL", "ARI", "LAA", "SDP", "SFG", "NYM", "MIL", "TOR", "COL", "PHI", "SEA", "MIN", "CHC", "CHW", "MIA", "HOU"],
            "AL_MVP": "Cabrera",
            "NL_MVP": "Ryan Braun",
            "AL_CY": "Max Scherzer",
            "NL_CY": "Clayton Kershaw"
        }

        self.assertTrue(request.get_method() == "PUT") # bit superfluous
        self.assertTrue(response.getcode() == 200)
        self.assertTrue(len(data) == 7)
        self.assertTrue(data == expected)
    
    def test_delete_years(self):
        headers = {"Content-Type": "application/json"}
    
        request = Request("http://mlbapi.apiary-mock.com/api/years/1", headers=headers)
        request.get_method = lambda: 'DELETE' 
        response = urlopen(request)

        self.assertTrue(response.getcode() == 204)
        self.assertTrue(request.get_method() == "DELETE") # bit superfluous

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
