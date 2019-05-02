from django.db import models
from datetime import datetime

# Create your models here.
# match_id, date, location, team1, team2, match_type, competition, winner, mom, win_wickets, win_run, toss_win, decision

class Matches(models.Model):
	match_id = models.IntegerField(null=False)
	date = models.DateTimeField(null=False)
	location = models.CharField(max_length=100, null=False)
	team1 = models.CharField(max_length=100, null=False)
	team2 = models.CharField(max_length=100, null=False)
	match_type = models.CharField(max_length=50, null=True)
	competition = models.CharField(max_length=50, null=True)
	winner = models.CharField(max_length=50, null=True)
	mom = models.CharField(max_length=50, null=True)
	win_wickets = models.IntegerField(null=True)
	win_run = models.IntegerField(null=True)
	toss_win = models.CharField(max_length=100, null=True)
	decision = models.CharField(max_length=100, null=True)

	# created_at = models.DateTimeField(default=datetime.now, blank=False)

	def __str__(self):
		return str(self.match_id)


class MatchDetails(models.Model):
	match_id = models.ForeignKey(Matches, on_delete=models.CASCADE)
	over = models.FloatField(null=False, default=None)
	runs = models.IntegerField(null=False)
	wickets = models.IntegerField(null=False)
	striker = models.CharField(max_length=100, null=False)
	non_striker = models.CharField(max_length=100, null=False)
	bowler = models.CharField(max_length=100, null=False)
	team = models.CharField(max_length=100, null=False, default=None)

	def __str__(self):
		return str(self.match_id)