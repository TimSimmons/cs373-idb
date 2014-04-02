from data.years import *
from data.players import *
from data.teams import *
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from models import *


def populate_years():
  for year in years:
    y = Year(**year)
    y.save()
  

def populate_teams():
  for team in teams:
    # Create a Team and Team_Image model
    t = Team(**team["team"])
    i = Team_Image(team=t, image=team["image"], kind="default")
    t.save()
    i.save()
    for team_year in team["years"]:
      y = Year.objects.get(year=team_year.pop("year", None))      
      ty = Team_Year(team=t, year=y, **team_year)
      ty.save()


def populate_players():
  for player in players:
    p = Player(**player["player"])
    i = Player_Image(image=player["image"], kind="default")
    p.save()
    i.save()
    for player_year in player["years"]:
      y = Year.objects.get(year=player_year.pop("year", None))
      t = Team.objects.get(name=player_year.pop("team", None))
      py = Player_Year(player=p, team=t, **player_year)
      py.save()

   