from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs): #*args, **kwargs
	# return HttpResponse("<h1> Welcome to Songnote</h1>") #string of html code
	return render(request,"home.html", {'user': request.user})

def musician_home_view(request, *args, **kwargs): #*args, **kwargs
	return render(request,"musician_home.html", {})

def listener_home_view(request, *args, **kwargs): #*args, **kwargs
	return render(request,"listener_home.html", {})

def leaderboard_view(request, *args, **kwargs): #*args, **kwargs
	my_context = {
		"my_text":"This is about me",
		"my_number": 123
	}
	return render(request,"leaderboard.html", my_context)

def feedback_view(request, *args, **kwargs): #*args, **kwargs
	return render(request,"feedback.html", {})

def questionnairesuccess_view(request, *args, **kwargs): #*args, **kwargs
	return render(request,"questionnairesuccess.html", {})

def successful_upload_view(request, *args, **kwargs): #*args, **kwargs
	return render(request,"successful_upload.html", {})


