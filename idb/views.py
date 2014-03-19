from django.shortcuts import render
import datetime
from django.http import HttpResponse
from idb.data import *

def home(request):
    return render(request, "index.html")

def player(request, player_id):
    if player_id == "01":
        return render(request, "player.html", bryce)
    return render(request, "player.html")

def team(request, team_id):
    if team_id == "20":
        return render(request, "team.html", angels)
    return render(request, "team.html")

def year(request, year_id):
    if year_id == "2013":
        return render(request, "year.html", year_2013 )
    return render(request, "year.html")

