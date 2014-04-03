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
  #POST
  if request.method == 'POST':
    body = json.loads(request.body)
    player = Player(**body)
    response = HttpResponse(serializers.serialize('json', [ player, ]), content_type="application/json")
  return response
  

@csrf_exempt
def team(request, team_id):
  team = Team.objects.get(id=team_id)
  if request.method == 'GET':
    response = HttpResponse(serializers.serialize('json', [ team, ]), content_type="application/json")
  return response
 

 
@csrf_exempt
def year(request, year_id):
  year = Year.objects.get(year=year_id)
  if request.method == 'GET':
    response = HttpResponse(serializers.serialize('json', [ year, ]), content_type="application/json")
  return response
