from djanga.db import models


class Player(models.Model):
	name = models.CharField(max_length=100)
	number = models.IntegerField()
	position = models.CharField(max_length=100)
	bat_handedness = models.CharField(max_length=100)
	throw_handedness = models.CharField(max_length=100)
	height = models.IntegerField()
	weight = models.IntegerField()
	school = models.CharField(max_length=100)
	twitter_handle = models.CharField(max_length=100)
	image = models.URLField()


class Team(model.Model):
	name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	park = models.CharField(max_length=100)
	division = models.CharField(max_length=100)
	team_years = models.CommaSeparatedIntegerField()
	twitter_handle = models.CharField(max_length=100)
	image = models.URLField()


class Year(model.Model):
	champion = models.CharField(Team)
	mvp_nl = models.CharField(Player)
	mvp_al = models.CharField(Player)
	cy_young_nl = models.CharField(Player)
	cy_young_al = models.CharField(Player)


class Player_Year(model.Model):
	player = models.ForeignKey(Player)
	team_year = models.ForeignKey(Team_Year)
	year = models.ForeignKey(Year)
	
	plate_appearances = models.IntegerField()
	games_played = models.IntegerField()
	batting_avg = models.FloatField()


class Team_Years(models.Model):
	team = models.ForeignKey(Team)
	year = models.ForeignKey(Year)
		
	wins = models.IntegerField()
	losses = models.IntegerField()
	manager = models.CharField()
	standing = models.IntegerField()
	playoffs = models.BooleanField()
	attendance = models.IntegerField()
	
	
		
