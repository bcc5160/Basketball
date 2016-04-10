from django.contrib import admin
from history.models import PastGame, ChanceWin

# Register your models here.
admin.site.register(PastGame)
admin.site.register(ChanceWin)