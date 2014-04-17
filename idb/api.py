from django.http import HttpResponse, Http404
from django.core import serializers
from idb.models import *
import json
import requests
from django.views.decorators.csrf import csrf_exempt
import sys
from django.utils import simplejson
import logging
import itertools
log = logging.getLogger(__name__)

@csrf_exempt
def player(request, player_id):
  # GET
  if request.method == 'GET':
    player = Player.objects.get(id=player_id)
    response = HttpResponse(serializers.serialize('json', [ player, ]), content_type="application/json")
  # PUT
  if request.method == 'PUT':
    player = Player.objects.get(id=player_id)
    body = json.loads(request.body.decode())
    for k,v in body.items():
      setattr(player, k, v)
      player.save() 
    response = HttpResponse(serializers.serialize('json', [ player, ]), content_type="application/json")
  #DELETE
  if request.method == 'DELETE':
    player = Player.objects.get(id=player_id)
    player.delete()
    response = HttpResponse()
    response.status_code = 204
  return response
  

@csrf_exempt
def players(request):
  #GET 
  if request.method == 'GET':
    players = Player.objects.all()
    response = HttpResponse(serializers.serialize('json', players), content_type="application/json")
  #POST
  if request.method == 'POST':
    body = json.loads(request.body.decode())
    response = HttpResponse(json.dumps(body), content_type="application/json")
    player = Player(**body)
    player.save()
    response = HttpResponse(serializers.serialize('json', [ player, ]), content_type="application/json")
    response.status_code = 201 
  return response  
  

@csrf_exempt
def team(request, team_id):
  #GET
  if request.method == 'GET':
    team = Team.objects.get(id=team_id)
    response = HttpResponse(serializers.serialize('json', [ team, ]), content_type="application/json")
  #PUT
  if request.method == 'PUT':
    team = Team.objects.get(id=team_id)
    body = json.loads(request.body.decode())
    for k,v in body.items():
      setattr(team, k, v)
      team.save()
    response = HttpResponse(serializers.serialize('json', [ team, ]), content_type="application/json")
  #DELETE
  if request.method == 'DELETE':
      team = Team.objects.get(id=team_id)
      team.delete()
      response = HttpResponse()
      response.status_code = 204
  return response
 

@csrf_exempt
def teams(request):
  #GET
  if request.method == 'GET':
    teams = Team.objects.all()
    response = HttpResponse(serializers.serialize('json', teams ), content_type="application/json")
  #POST
  if request.method == 'POST':
    body = json.loads(request.body.decode())
    team = Team(**body)
    team.save()
    response = HttpResponse(serializers.serialize('json', [ team, ]), content_type="application/json")
    response.status_code = 201  
  return response

 
@csrf_exempt
def year(request, year_id):
  #GET
  if request.method == 'GET':
    year = Year.objects.get(year=year_id)
    response = HttpResponse(serializers.serialize('json', [ year, ]), content_type="application/json")
  #PUT
  if request.method == 'PUT':
    year = Year.objects.get(year=year_id)
    body = json.loads(request.body.decode())
    for k,v in body.items():
      setattr(year, k, v)
      year.save()
    response = HttpResponse(serializers.serialize('json', [ year, ]), content_type="application/json")
    response.status_code = 200
  #DELETE
  if request.method == 'DELETE':
    year = Year.objects.get(year=year_id)
    year.delete()
    response = HttpResponse()
    response.status_code = 204
  return response


@csrf_exempt
def years(request):
  #GET 
  if request.method == 'GET':
    years = Year.objects.all()
    response = HttpResponse(serializers.serialize('json', years), content_type="application/json")
  #POST
  if request.method == 'POST':
    body = json.loads(request.body.decode())
    year = Year(id=body["year"], **body)
    year.save()
    response = HttpResponse(serializers.serialize('json', [ year, ]), content_type="application/json")
    response.status_code = 201
  return response

  
@csrf_exempt
def player_years(request, player_id):
  """
      players/{id}/years
  """
  #GET 
  if request.method == 'GET':
    player = Player.objects.get(id=player_id)
    player_years = player.years.all()
    response = HttpResponse(serializers.serialize('json', player_years), content_type="application/json")
  #POST
  if request.method == 'POST':
    body = json.loads(request.body.decode())   
    player = Player.objects.get(id=player_id)
    year = Year.objects.get(year=body.pop("year", None))
    team = Team.objects.get(name=body.pop("team", None))
    team_year = Team_Year.objects.get(team=team, year=year)

    body["avg"] = float(body["avg"])
    body["obp"] = float(body["obp"])
    body["slg"] = float(body["slg"])
    # return HttpResponse(json.dumps(body))
    player_year = Player_Year(year=year, player=player, team_year=team_year, **body)
    player_year.save()

    response = HttpResponse(serializers.serialize('json', [ player_year, ]), content_type="application/json")
    response.status_code = 201
  return response  
  
  
@csrf_exempt
def player_year(request, player_id, year_id):
  """
      players/{id}/years/{year}
  """
  player = Player.objects.get(id=player_id)
  py_key = player.years.filter(year=year_id)
  player_year = Player_Year.objects.get(pk=py_key)
  if request.method == 'GET':
    player = Player.objects.get(id=player_id)
    py_key = player.years.filter(year=year_id)
    player_year = Player_Year.objects.get(pk=py_key)
    response = HttpResponse(serializers.serialize('json', [ player_year, ]), content_type="application/json")
  if request.method == 'PUT':
    body = json.loads(request.body.decode())
    for k,v in body.items():
      setattr(player_year, k, v)
      player_year.save()
      response = HttpResponse(serializers.serialize('json', [ player_year, ]), content_type="application/json")
  if request.method == 'DELETE':
    player_year.delete()
    response = response = HttpResponse()
    response.status_code = 204
  return response
  

@csrf_exempt
def team_years(request, team_id):
  """
      teams/{id}/years
  """
  if request.method == 'GET':
    team = Team.objects.get(id=team_id)
    team_years = team.years.all()
    response = HttpResponse(serializers.serialize('json', team_years), content_type="application/json")
  if request.method == 'POST':
    body = json.loads(request.body.decode())
    team = Team.objects.get(id=team_id)
    year = Year.objects.get(year=body.pop("year", None))
    team_year = Team_Year(year=year, team=team, **body)
    team_year.save()
    response = HttpResponse(serializers.serialize('json', [ team_year, ]), content_type="application/json")
    response.status_code = 201
  return response
  
  
@csrf_exempt
def team_year(request, team_id, year_id):
  """
    teams/{id}/years/{id}
  """
  team = Team.objects.get(id=team_id)
  ty_key = team.years.filter(year=year_id)
  team_year = Team_Year.objects.get(pk=ty_key)
  if request.method == 'GET':
    response = HttpResponse(serializers.serialize('json', [ team_year, ]), content_type="application/json")
  if request.method == 'PUT':
    body = json.loads(request.body.decode())
    for k,v in body.items():
      setattr(team_year, k, v)
      team_year.save()
      response = HttpResponse(serializers.serialize('json', [ team_year, ]), content_type="application/json")
  if request.method == 'DELETE':
    team_year.delete()
    response = response = HttpResponse()
    response.status_code = 204
  return response
  
@csrf_exempt
def search(request, q):
  q = q.replace('%20', ' ').split(' ')
  perm = []
  for x in range(1, len(q)+1):
    perm.append(list(itertools.permutations(q, x)))
  comb = []
  for x in perm:
      for i in x:
        comb.append(' '.join(a for a in i))


  teams = []
  for z in comb:
    for t in Team.query(z):
      temp = t.to_dict()
      if temp not in teams:
        teams.append(temp)
  # list(t.to_dict() for t in Team.query(z) for z in comb)
  # players = [p.to_dict() for p in Player.query(q)]
  players = []
  for z in comb:
    for t in Player.query(z):
      temp = t.to_dict()
      if temp not in players:
        players.append(temp)
  # years = [y.to_dict() for y in Year.query(q)]
  years = []
  for z in comb:
    for t in Year.query(z):
      temp = t.to_dict()
      if temp not in years:
        years.append(temp)
  d = dict(num_results=len(teams) + len(players) + len(years) ,teams=teams, players=players, years=years)
  return HttpResponse(simplejson.dumps(d), mimetype='application/json')

#New York Yankees Mike
#Mike Trout Miguel