from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def profile_detail_view(request):
	obj = Profile.objects.get(id=1)
	#songs = Song.objects.filter(listener_id=request.user)
	context = {
		'object': obj,
		#songs': songs,
	}
	return render(request,"profile/detail.html", context)

