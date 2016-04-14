import math, random
from django.shortcuts import render
from .models import PastGame, ChanceWin
from django.template import Context, loader

# Create your views here.
def show(request):
	#random = random.seed() % 16
	teams = ChanceWin.objects.values('team1Seed')
	allTeam = PastGame.objects.all()

	context = {
		"allTeam" : allTeam,
	}

	#for i in team1:


	return render(request, 'south.html', context)
