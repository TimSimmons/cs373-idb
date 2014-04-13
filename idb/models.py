from django.db import models


class Player(models.Model):
    """
    Contains static information about a player.

    The Player model serves as somewhat of a parent class and container
    to the Player_Year model. Each Player model contains information
    about an individual player which remains persistent throughout a
    player's career. For example, a player's name, school and handedness
    are contained in this model.

    The Player model has a one to many relationship with the Player_Year model.
    """
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    position = models.CharField(max_length=3)
    bats = models.CharField(max_length=1)
    throws = models.CharField(max_length=1)
    height = models.IntegerField()
    weight = models.IntegerField()
    school = models.CharField(max_length=50)
    social = models.CharField(max_length=30)
    
    def gen_link(self):
        return "/players/"+str(self.id)

    def __unicode__(self):
        return self.name
        
class Team(models.Model):
    """
    Conatins static information about a team.

    The Team model serves a purpose similar to the Player model in that it
    contains information about a team that generally does not change through
    the years.

    The Team model has a one to many relationship with the Team_Year model.
    """
    name = models.CharField(max_length=30)
    abbr = models.CharField(max_length=3)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    park = models.CharField(max_length=30)
    div = models.CharField(max_length=10)
    mgr = models.CharField(max_length=30)
    social = models.CharField(max_length=30)
    
    def __str__(self):
      return "name: " + self.name + \
             "\nabbr: " + self.abbr + \
             "\ncity: " + self.city + \
             "\nstate: " + self.state + \
             "\npark: " + self.park + \
             "\ndiv: " + self.div + \
             "\nmgr: " + self.mgr + \
             "\nsocial: " + self.social
      
    def gen_link(self):
      return "/teams/"+self.abbr


class Year(models.Model):
    """
    Contains information about award winners for a given year.

    The Year model serves as a filter for standings across teams for a particular
    year as well as awards for individual players for that year.

    The Year model has a one to many relationship with the Player_Year and Team_Year models.
    """
    year = models.CharField(max_length=4)
    champion = models.CharField(max_length=30)
    AL_MVP = models.CharField(max_length=30)
    NL_MVP = models.CharField(max_length=30)
    NL_CY = models.CharField(max_length=30)
    AL_CY = models.CharField(max_length=30)

    def gen_link(self):
      return "/years/"+self.year


class Team_Year(models.Model):
    """
    Contains team statistics for a given year.

    The Team_Year model, like the Player_Year model, contains information about a
    team for a spicific year.


    The Team_Yeam model has a many to one relationship with the Year and Team models.
    """
    team = models.ForeignKey(Team, related_name='years')
    year = models.ForeignKey(Year, related_name='team_years')
    wins = models.IntegerField()
    losses = models.IntegerField()
    standing = models.IntegerField()
    playoffs = models.CharField(max_length=20)
    attend = models.IntegerField()
    payroll = models.IntegerField()
    
    def __str__(self):
      return "team: " + self.team.name + \
    	     "\nyear: " + self.year.year + \
    	     "\nwins: " + str(self.wins) + \
    	     "\nlosses: " + str(self.losses) + \
    	     "\nstanding: " + str(self.standing) + \
    	     "\nplayoffs: " + self.playoffs + \
    	     "\nattend: " + str(self.attend) + \
    	     "\npayroll: " + str(self.payroll)

class Player_Year(models.Model):
    """
    Contains player statistics for a given year.

    The Player_Year model holds information about a player which
    is likely to change from year to year. For example, any yearly
    statistics such as batting average or the team the player played
    for that specific year would be attributes of this model.

    The Player_Year model has a many to one relationship with the Team_Year, Year, and
    Player models.
    """
    player = models.ForeignKey(Player, related_name='years')
    team_year = models.ForeignKey(Team_Year, related_name='player_years') 
    year = models.ForeignKey(Year, related_name='player_years')
    games = models.IntegerField()
    kind = models.CharField(max_length=10) #choices = hitter/pitcher
    # hitting stats
    pa = models.IntegerField(blank=True, null=True)
    avg = models.FloatField(blank=True, null=True)
    obp = models.FloatField(blank=True, null=True)
    slg = models.FloatField(blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)
    rbi = models.IntegerField(blank=True, null=True)
    #pitching stats
    w = models.IntegerField(blank=True, null=True)
    l = models.IntegerField(blank=True, null=True)
    era = models.FloatField(blank=True, null=True)
    gs = models.IntegerField(blank=True, null=True)
    s = models.IntegerField(blank=True, null=True)
    ip = models.IntegerField(blank=True, null=True)
    whip = models.FloatField(blank=True, null=True)

    	     
class Player_Image(models.Model):
    """
    Model representation of an image that is associated with a player. 
    """
    player = models.ForeignKey(Player, related_name='images')
    image = models.URLField() #might need type, but not sure what for
    kind = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
      return "player: " + str(self.player.name) + \
    	     "\nimage: " + str(self.image) + \
    	     "\nkind: " + str(self.kind)
    
class Team_Image(models.Model):
    """
    Model representation of an image that is associated with a team. 
    """
    team = models.ForeignKey(Team, related_name='images')
    image = models.URLField()
    kind = models.CharField(max_length=10, blank=True, null=True) #choices logo/park?
  
    def __str__(self):
      return "team: " + str(self.team.name) + \
    	     "\nimage: " + str(self.image) + \
    	     "\nkind: " + str(self.kind)
