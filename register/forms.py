from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('Name', 'User_type','city_of_residence')

	def __init__(self, *args, **kwargs):
		self._user = kwargs.pop('user')
		super(ProfileForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		inst = super(ProfileForm, self).save(commit=False)
		inst.user = self._user
		if commit:
			inst.save()
			self.save_m2m()
		return inst
		
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
    	model = User
    	fields = ["username", "email", "password1", "password2",]
    #def __init__(self, *args, **kwargs):
    	#self._user = kwargs.pop('user')
    	#super(RegisterForm, self).__init__(*args, **kwargs)
    #def save(self, commit=True):
    	#inst = super(RegisterForm, self).save(commit=False)
    	#inst.user = self._user
    	#if commit:
    		#inst.save()
    		#self.save_m2m()
    		#return inst


 

