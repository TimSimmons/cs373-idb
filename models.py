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
	years = models.ManyToManyField(Year)
	twitter_handle = models.CharField(max_length=100)
	image = models.URLField()


class Team(model.Model):
	name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	park = models.CharField(max_length=100)
	division = models.CharField(max_length=100)
	years = models.ManyToManyField(Year)
	twitter_handle = models.CharField(max_length=100)
	image = models.URLField()


class Year(model.Model):
	#?standings
	player_years = models.ManyToManyField(Player_Year)
	team_years = models.ManyToManyField(Team_Year)
	champion = models.ForeignKey(Team)
	mvp_nl = models.ForeignKey(Player)
	mvp_al = models.ForeignKey(Player)
	cy_young_nl = models.ForeignKey(Player)
	cy_young_al = models.ForeignKey(Player)


class Player_Year(model.Model):
	year = models.ForeignKey(Year)
	team = models.ForeignKey(Team)
	plate_appearances = models.IntegerField()
	games_played = models.IntegerField()
	batting_avg = models.CharField(max_length=10)


class Team_Years(models.Model):
		