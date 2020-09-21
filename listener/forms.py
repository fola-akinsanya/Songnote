from django import forms
from .models import ListenerQuestionnaire, ListenerFeedback

class ListenerQuestionnaireForm(forms.ModelForm):
	class Meta:
		model = ListenerQuestionnaire
		fields = ('age_range', 'gender','ethnic_group','favourite_genre','artists_you_listen_to','favourite_hangout_spots')

class ListenerFeedbackForm(forms.ModelForm):
	class Meta:
		model = ListenerFeedback
		fields = ('playlist', 'production_value','lyrical_value', 'vocal_perf','listen_again','listen_another','watch_live','hit')
		labels= {
			'playlist': ('Would you playlist this song?'),
			'production_value':('What would you rate the production value out of 5?'),
			'lyrical_value': ('What would you rate the lyrical value out of 5?'),
			'vocal_perf': ('What would you rate the vocal performance out of 5?'),
			'listen_again': ('Would you listen to this song again?'),
			'listen_another': ("Would you listen to another of this artist's songs?"),
			'watch_live': ("Would you watch this musician perform live?"),
			'hit': ("Do you think this song could be a hit?")
		}