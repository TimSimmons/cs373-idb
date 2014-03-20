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
    school = models.CharField(max_length=30)
    social = models.CharField(max_length=30)
    image = models.URLField()


class Team(model.Model):
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
    images = models.URLField()


class Year(model.Model):
    """
    Contains information about award winners for a given year.

    The Year model serves as a filter for standings across teams for a particular
    year as well as awards for individual players for that year.


    The Year model has a one to many relationship with the Player_Year and Team_Year models.
    """
    champion = models.CharField(max_length=30)
    AL_MVP = models.CharField(max_length=30)
    NL_MVP = models.CharField(max_length=30)
    NL_CY = models.CharField(max_length=30)
    AL_CY = models.CharField(max_length=30)


class Player_Year(model.Model):
    """
    Contains player statistics for a given year.

    The Player_Year model holds information about a player which
    is likely to change from year to year. For example, any yearly
    statistics such as batting average or the team the player played
    for that specific year would be attributes of this model.


    The Player_Year model has a many to one relationship with the Team_Year, Year, and
    Player models.
	"""
    player = models.ForeignKey(Player, related_name='player_years')
    team_year = models.ForeignKey(Team_Year, related_name='player_years')
    year = models.ForeignKey(Year, related_name='player_years')
    # hitting stats
    pa = models.IntegerField()
    games = models.IntegerField()
    avg = models.FloatField()
    obp = models.FloatField()
    slg = models.FloatField()
    hr = models.IntegerField()
    rbi = models.IntegerField()
    #pictching stats
    wins = models.IntegerField()
    losses = models.IntegerField()
    era = models.FloatField()
    games_pitched = models.IntegerField()
    games_started = models.IntegerField()
    saves = models.IntegerField()
    innings_pitched = models.IntegerField()
    walks_per_inning = models.FloatField()
    pitched = models.Floatfield()


class Team_Years(models.Model):
    """
    Contains team statistics for a given year.

    The Team_Year model, like the Player_Year model, contains information about a
    team for a spicific year.


    The Team_Yeam model has a many to one relationship with the Year and Team models.
    """
    team = models.ForeignKey(Team, related_name='team_years')
    year = models.ForeignKey(Year, related_name='team_years')
    wins = models.IntegerField()
    losses = models.IntegerField()
    manager = models.CharField(max_length=20)
    standing = models.IntegerField()
    playoffs = models.CharField(max_length=20)
    attend = models.IntegerField()
    payroll = models.IntegerField()