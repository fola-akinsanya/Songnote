from django.shortcuts import render
from .models import Leaderboard

# Create your views here.
def leaderboard_view(request):
	leaderboard_results = Leaderboard.objects.all()
	context = {'leaderboard_results': leaderboard_results}
	return render(request,"leaderboard.html", context)