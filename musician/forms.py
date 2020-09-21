from django import forms

from .models import SongUpload

class UploadForm(forms.ModelForm):
	class Meta:
		model = SongUpload
		fields = ('title','song_genre', 'song')