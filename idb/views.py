from django.shortcuts import render
import datetime
from django.http import HttpResponse
from idb.data import *

def home(request):
    return render(request, "index.html")

def player(request, player_id):
    if player_id == "01":
        return render(request, "player.html", bryce)
    if player_id == "02":
        return render(request, "player.html", yu)
    if player_id == "03":
        return render(request, "player.html", mike)
    return render(request, "player.html")

def team(request, team_id):
    team_id = team_id.lower()
    if team_id == "laa":
        return render(request, "team.html", angels)
    if team_id == "stl":
        return render(request, "team.html", cardinals)
    if team_id == "lad":
        return render(request, "team.html", dodgers)
    if team_id == "wsn":
        return render(request, "team.html", nationals)
    if team_id == "fla":
        return render(request, "team.html", marlins)
    if team_id == "min":
        return render(request, "team.html", twins)
    if team_id == "bos":
        return render(request, "team.html", redsox)
    if team_id == "nyy":
        return render(request, "team.html", yankees)
    if team_id == "pit":
        return render(request, "team.html", pirates)
    if team_id == "det":
        return render(request, "team.html", tigers)
    return render(request, "team.html")

def year(request, year_id):
    if year_id == "2013":
        return render(request, "year.html", year_2013 )
    if year_id == "2012":
        return render(request, "year.html", year_2012 )
    if year_id == "2011":
        return render(request, "year.html", year_2011 )
    if year_id == "2010":
        return render(request, "year.html", year_2010 )
    if year_id == "2009":
        return render(request, "year.html", year_2009 )
    if year_id == "2008":
        return render(request, "year.html", year_2008 )
    if year_id == "2007":
        return render(request, "year.html", year_2007 )
    if year_id == "2006":
        return render(request, "year.html", year_2006 )
    if year_id == "2005":
        return render(request, "year.html", year_2005 )
    if year_id == "2004":
        return render(request, "year.html", year_2004 )
    return render(request, "year.html")
