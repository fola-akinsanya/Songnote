from django.contrib import admin

# Register your models here.
from .models import Profile

#class CustomUserAdmin():
	#standardregister_form = RegisterForm
	#standardprofile_form= ProfileForm
	#models = User, Profile
	#list_display = ["Name", "User_Type", "username", "email", "password1", "password2"]

admin.site.register(Profile)


