from django.http import HttpResponse, Http404
from django.core import serializers
from idb.models import *
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def player(request, player_id):
    # GET
    if request.method == 'GET':
      player = Player.objects.get(id=player_id)
      response = HttpResponse(serializers.serialize('json', [ player, ]), content_type="application/json")
    # PUT
    if request.method == 'PUT':
      player = Player.objects.get(id=player_id)
      body = json.loads(request.body)
      for k,v in body.items():
	setattr(player, k, v)
	player.save() 
      response = HttpResponse(serializers.serialize('json', [ player, ]), content_type="application/json")
    return response
  

@csrf_exempt
def players(request):
  #GET 
  if request.method == 'GET':
    players = Player.objects
    response = HttpResponse(serializers.serialize('json', players), content_type="application/json")
  #POST
  if request.method == 'POST':
    body = json.loads(request.body)
    player = Player(**body)
    response = HttpResponse(serializers.serialize('json', [ player, ]), content_type="application/json")
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
    for k,v in body.items():
      setattr(team, k, v)
      team.save()
    response = HttpResponse(serializers.serialize('json', [ team, ]), content_type="application/json")
  return response
 

@csrf_exempt
def teams(request):
  #GET
  if request.method == 'GET'
    teams = Team.objects
    response = HttpResponse(serializers.serialize('json', teams ), content_type="application/json")
  #POST
  if request.method == 'POST':
    body = json.loads(request.body)
    team = Team(**body)
    response = HttpResponse(serializers.serialize('json', [ team, ]), content_type="application/json")
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
    for k,v in body.items():
      setattr(year, k, v)
      year.save()
    response = HttpResponse(serializers.serialize('json', [ year, ]), content_type="application/json")
  return response


@csrf_exempt
def years(request):
  #GET 
  if request.method == 'GET':
    years = Year.objects
    response = HttpResponse(serializers.serialize('json', years), content_type="application/json")
  #POST
  if request.method == 'POST':
    body = json.loads(request.body)
    year = Year(**body)
    response = HttpResponse(serializers.serialize('json', [ year, ]), content_type="application/json")
  return response