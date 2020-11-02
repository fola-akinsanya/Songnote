from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import ProfileForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
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
		profile_form=ProfileForm()

	return render(request, "register/register-2.html", {"profile_form": profile_form})

def edit_profile_view(request):
	if request.method =="POST":
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
		form = EditProfileForm(instance=request.user)
		return render(request, 'registration/edit_profile.html', {'form':form})

def change_password_view(request):
	if request.method =="POST":
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('registration/passwordchangesuccess.html')

	else:
		form = PasswordChangeForm(user=request.user)
		return render(request, 'registration/change_password.html', {'form':form})

























