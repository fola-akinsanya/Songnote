from django import forms
from .models import ListenerQuestionnaire

class ListenerQuestionnaireForm(forms.ModelForm):
	class Meta:
		model = ListenerQuestionnaire
		fields = ('age_range', 'ethnic_group','favourite_genre','artists_you_listen_to','favourite_hangout_spots')