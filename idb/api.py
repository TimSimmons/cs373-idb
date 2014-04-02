from django.http import HttpResponse, Http404
from django.core import serializers
from idb.models import *
import json

def api_player(request, player_id):
  player = Player.objects.get(id=player_id)
  if request.method == 'GET':
    response = HttpResponse(serializers.serialize('json', [ player, ]), content_type="application/json")
  return response