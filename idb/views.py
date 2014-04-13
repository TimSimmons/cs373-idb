from django.shortcuts import render
from django.http import HttpResponse, Http404
from idb.data import *
from idb.models import *
from idb.clientside import clientside
import json

def home(request):
    return render(request, "index.html")

def player(request, player_id):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
       raise Http404
    return render(request, "player.html", {'player':player} )

def team(request, team_id):
    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
       raise Http404
    return render(request, "team.html", {'team':team} )

def team_abbr(request, team):
    try:
        team = Team.objects.get(abbr=team)
    except Team.DoesNotExist:
       raise Http404
    return render(request, "team.html", {'team':team} )

def year(request, year_id):
    try:
        year = Year.objects.get(year=year_id)
        team_years = year.team_years.all().order_by('-wins')
        #standings = json.loads(year.standings)
    except Year.DoesNotExist:
       raise Http404
    return render(request, "year.html", {'year':year, 'standings':team_years} )

def players(request):
    try:
        players = Player.objects.all().order_by('name')
    except:
       raise Http404
    return render(request, "player-list.html", {'players':players} )

def teams(request):
    try:
        teams = Team.objects.all().order_by('name')
    except:
       raise Http404
    return render(request, "team-list.html", {'teams':teams} )

def years(request):
    try:
        years = Year.objects.all().order_by('year')
    except:
       raise Http404
    return render(request, "year-list.html", {'years':years} )

def sql(request):
    return render(request, "sql.html")