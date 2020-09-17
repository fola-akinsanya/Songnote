from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile


# Create your views here.
def register_view(request):
	if request.method == "POST":
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			new_user= register_form.save()
			new_user = register_form.save()
			#messages.info(request, "Thanks for registering. You are now logged in.")
			new_user = authenticate(username=register_form.cleaned_data['username'],
            	password=register_form.cleaned_data['password1'],
            	)
			login(request, new_user)

			return redirect("register-2")
	else:
		register_form = RegisterForm()
		

	return render(request, "register/register.html", {"register_form":register_form })

def profile_view(request):
	if request.method == "POST":
		profile_form = ProfileForm(request.POST,user= request.user)
		if profile_form.is_valid():
			new_profile= profile_form.save()
			usertype= new_profile.User_type
			if usertype=='listener':
				return redirect("questionnaire")
			else:
				return redirect("home")
	else: 
		profile_form=ProfileForm(request.POST, user= request.user)

	return render(request, "register/register-2.html", {"profile_form": profile_form})



#def register_view(response):
	#if response.method == "POST":
		#form = RegisterForm(response.POST)
		#if form.is_valid():
			#form.save()

		#return redirect("home")
	#else:
		#form = RegisterForm()

	#return render(response, "register/register.html", {"form":form})