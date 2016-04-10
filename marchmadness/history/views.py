import math, random
from django.shortcuts import render
from .models import PastGame, ChanceWin

# Create your views here.
def show(request):
	#random = random.seed() % 16
	team1 = ChanceWin.objects.values('team1Seed')
	team2 = ChanceWin.objects.values('team2Seed')
	

	#for i in team1:


	return render(request, 'index.html', {})
