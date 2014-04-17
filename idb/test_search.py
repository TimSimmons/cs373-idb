#!/usr/bin/env python3
from django.test import TestCase
import unittest
import requests
from json import dumps


url_search = "http://frozen-plateau-5382.herokuapp.com/api/search/"


def mget(q):
    r = requests.get(url_search + q)
    return r.json()


class TestSearchSingle1(TestCase):
    
    def test_single_player_1(self):
        query = "Mike"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["players"]) != 0)
        self.assertTrue(data["players"][0]["name"].split(' ')[0] == "Mike")
        
    def test_single_partial_1(self):
        query = "Mi"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["players"]) != 0)
        
    def test_single_num_1(self):
        query = "4"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
    
    def test_single_year_1(self):
        query = "2004"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(data["years"][0]["year"] == "2004")
    
    def test_single_team_1(self):
        query = "Cardinals"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["teams"]) != 0)
        self.assertTrue(data["teams"][0]["name"] == "St. Louis Cardinals")
        
    def test_single_player_lower_1(self):
        query = "mike"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["players"]) != 0)
        self.assertTrue(data["players"][0]["name"].split(' ')[0] == "Mike")
        
    def test_single_team_case_lower_1(self):
        query = "Cardinals"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["teams"]) != 0)
        self.assertTrue(data["teams"][0]["name"] == "St. Louis Cardinals")
        
        
    def test_single_player_case_upper_1(self):
        query = "MIKE"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["players"]) != 0)
        self.assertTrue(data["players"][0]["name"].split(' ')[0] == "Mike")
     
    def test_single_team_case_upper_1(self):
        query = "CARDINALS"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["teams"]) != 0)
        self.assertTrue(data["teams"][0]["name"] == "St. Louis Cardinals")
        
        
class TestSearchNoMatch(TestCase):
    
    def test_no_match_1(self):
        q = "alsjhdfkajfh"
        r = requests.get(url_search + q)
        r.status_code == 404

    def test_no_match_2(self):
        q = "alsjhdfkajfh"
        r = requests.get(url_search + q)
        r.status_code == 404
        
    def test_no_match_3(self):
        q = "alsjhdfkajfh"
        r = requests.get(url_search + q)
        r.status_code == 404
    
    
class TestSearchDouble(TestCase):
    
    def test_double_player_1(self):
        query = "asdsa Cabrera"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["players"]) != 0)
    
    def test_double_player_2(self):
        query = "Cabrera sdfgf"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["players"]) != 0)
    
    def test_double_team_1(self):
        query = "asdas Cardinals"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["teams"]) != 0)
        self.assertTrue(data["teams"][0]["name"] == "St. Louis Cardinals")
        
    def test_double_team_2(self):
        query = "Cardinals sdfsdf"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["teams"]) != 0)
        self.assertTrue(data["teams"][0]["name"] == "St. Louis Cardinals")
        
    def test_double_year_1(self):
        query = "asdas 2009"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["years"]) != 0)
        self.assertTrue(data["years"][0]["year"] == "2009")
        
    def test_double_year_2(self):
        query = "2009 sdfsdf"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["years"]) != 0)
        self.assertTrue(data["years"][0]["year"] == "2009")
        
        
class TestSearchTriple(TestCase):
  
    def test_triple_word_1(self):
        query = "Mike Cabrera Cardninals"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] != 0)
        self.assertTrue(len(data["players"]) != 0)
        self.assertTrue(len(data["teams"]) != 0)
       
    def test_triple_partial_all_1(self):
        query = "Mi 004 Tex"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] > 2)
        self.assertTrue(len(data["players"]) != 0)
        self.assertTrue(len(data["teams"]) != 0)
        self.assertTrue(len(data["years"]) != 0)
        
    def test_triple_num_1(self):
        query = "6 7 8"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] > 2)
        self.assertTrue(len(data["years"]) > 2)
        
    def test_triple_team_partial_1(self):
        query = "Tex Card Yor"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] > 2)
        self.assertTrue(len(data["teams"]) > 2)
    
    def test_triple_team_full_1(self):
        query = "Texas Cardinals York"
        data = mget(query)
        self.assertTrue(len(data) != 0)
        self.assertTrue(data["num_results"] > 2)
        self.assertTrue(len(data["teams"]) > 2)
    
