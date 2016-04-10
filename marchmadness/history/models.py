from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PastGame(models.Model):
	gameID = models.IntegerField(default = 0)
	team = models.CharField(max_length=255, default="")
	teamSeed = models.IntegerField()
	gameRound = models.IntegerField()
	winner = models.IntegerField()

class ChanceWin(models.Model):
	gameID = models.IntegerField(default = 0)
	team1 = models.CharField(max_length=255, default="")
	team2 = models.CharField(max_length=255, default="")
	team1Seed = models.IntegerField(default=0)
	team2Seed = models.IntegerField(default=0)
	gameRound = models.IntegerField(default=0)
	winPer1 = models.DecimalField(max_digits=6, decimal_places=2)




 