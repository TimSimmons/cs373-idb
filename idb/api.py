from django.http import HttpResponse, Http404
from django.core import serializers
from idb.models import *
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def player(request, player_id):
  player = Player.objects.get(id=player_id)
  if request.method == 'GET':
    response = HttpResponse(serializers.serialize('json', [ player, ]), content_type="application/json")
  if request.method == 'PUT':
    body = json.loads(request.body)
    for k,v in body.items():
      setattr(player, k, v)
      player.save()  
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
