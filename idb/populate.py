from data1 import *
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from models import *

#years = [year_2012, year_2011, year_2010, year_2009, year_2008, year_2007, year_2006, year_2005, year_2004]


print "imported"

def populate_years():
  for year in years:
    y = Year(**year)
    y.save()
  print Year.objects.all()
  
def populate_teams():
  for team in teams:
    # Create a Team and Team_Image model
    t = Team(**team["team"])
    i = Team_Image(team=t, image=team["image"], type="default")
    
    t.save()
    i.save()
    
    print "\n" + str(t) 
    print "\n" + str(i)
    
    for team_year in team["years"]:
      # use the 'year' value to grab the associated year model
      year_val = team_year["year"]
      y = Year.objects.get(year=team_year["year"])
      print str(y.year)
      
      # remove year so we can unpack, maybe could have done this earlier
      team_year.pop("year", None)
      ty = Team_Year(team=t, year=y, **team_year)
      
      print str(ty)
      
      ty.save()
    #endfor