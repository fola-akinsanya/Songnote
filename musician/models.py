from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.conf import settings


# Create your models here.
class SongUpload(models.Model):

	def ___str___(self):
		return self.title

	SONG_GENRE = [
		('rap','Rap'),
		('rnb', 'RnB'),
		('drill','Drill'),
		('hip hop','Hip Hop'),
		('grime','Grime'),
		('afro swing','Afro Swing'),
		('reggae','Reggae'),
		('pop','Pop'),
		('dubstep','Dubstep'),
		('jazz','Jazz'),
		('drum and bass','Drum and Bass'),
		('rock','Rock'),
		('heavy metal','Heavy Metal')
	]
	artist = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=100)
	song_genre = models.CharField(max_length=100, choices=SONG_GENRE)
	song = models.FileField(upload_to='media/songs')



