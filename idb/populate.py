from data.years import *
from data.players import *
from data.teams import *
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from models import *


def populate_years():
  for year in years:
    y = Year(id=year["year"]["year"], **year["year"])
    i = Year_Image(year=y, image=year["image"], kind="default")
    y.save()
    i.save()

def populate_teams():
  for team in teams:
    # Create a Team and Team_Image model
    t = Team(**team["team"])
    t.save()
    i = Team_Image(team=t, image=team["image"], kind="default")
    i.save()
    for team_year in team["years"]:
      y = Year.objects.get(year=team_year.pop("year", None))      
      ty = Team_Year(team=t, year=y, **team_year)
      ty.save()


def populate_players():
  for player in players:
    p = Player(**player["player"])
    p.save()
    i = Player_Image(player=p, image=player["image"], kind="default")
    i.save()
    for player_year in player["years"]:
      y = Year.objects.get(year=player_year.pop("year", None))
      t = Team.objects.get(name=player_year.pop("team", None))
      
      # get the associated team_year
      tyk = y.team_years.filter(team=t)
      ty = Team_Year.objects.get(pk=tyk)
      print ty
      py = Player_Year(player=p, team_year=ty, year=y ,**player_year)
      py.save()

def populate_all():
  populate_years()
  populate_teams()
  populate_years()