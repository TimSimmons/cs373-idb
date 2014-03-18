from django.db import models


class Player(models.Model):
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
	champion = models.CharField(max_length=30)
	AL_MVP = models.CharField(max_length=30)
	NL_MVP = models.CharField(max_length=30)
	NL_CY = models.CharField(max_length=30)
	AL_CY = models.CharField(max_length=30)


class Player_Year(model.Model):
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
	team = models.ForeignKey(Team, related_name='team_years')
	year = models.ForeignKey(Year, related_name='team_years')

	wins = models.IntegerField()
	losses = models.IntegerField()
	manager = models.CharField(max_length=20)
	standing = models.IntegerField()
	playoffs = models.CharField(max_length=20)
	attend = models.IntegerField()
	payroll = models.IntegerField()
