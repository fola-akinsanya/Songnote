from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile



class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('User_type','city_of_residence')

	def __init__(self, *args, **kwargs):
		if 'user' in kwargs:
			self._user = kwargs.pop('user')
		super(ProfileForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		inst = super(ProfileForm, self).save(commit=False)
		if  self._user:
			inst.user = self._user
		if commit:
			inst.save()
			self.save_m2m()
		return inst
		
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
    	model = User
    	fields = ["first_name", "last_name","username", "email", "password1", "password2",]

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password']
		help_texts = {
		'password': ('Use the link below to update your password'),
		}




 

