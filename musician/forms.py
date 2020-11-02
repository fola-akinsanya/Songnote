from django import forms

from .models import SongUpload

class UploadForm(forms.ModelForm):
	class Meta:
		model = SongUpload
		fields = ('title','song_genre', 'song')

	def __init__(self, *args, **kwargs):
		if 'artist' in kwargs:
			self._artist = kwargs.pop('artist')
		super(UploadForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		inst = super(UploadForm, self).save(commit=False)
		if  self._artist:
			inst.artist = self._artist
		if commit:
			inst.save()
			self.save_m2m()
		return inst