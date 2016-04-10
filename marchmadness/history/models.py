from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PastGame(models.Model):
	gameID = models.IntegerField(default = 0)
	team1Seed = models.IntegerField()
	team2Seed = models.IntegerField()
	gameRound = models.IntegerField()
	winner = models.IntegerField()

class ChanceWin(models.Model):
	gameID = models.IntegerField(default = 0)
	team1Seed = models.IntegerField()
	team2Seed = models.IntegerField()
	gameRound = models.IntegerField()
	winT1 = models.DecimalField(max_digits=6, decimal_places=2)




 