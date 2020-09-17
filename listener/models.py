from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse



# Create your models here.
class ListenerQuestionnaire(models.Model):
	AGE_RANGE = [
		('16-19', '16-19'),
		('20-24', '20-24'),
		('25-34','25-34'),
		('35-44','35-44'),
		('45-54','45-54'),
		('55-64','55-64'),
		('65+','65+')
	]
	GENDER = [
		('male','Male'),
		('female','Female')
	]
	MUSIC_GENRE = [
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
	ETHNIC_GROUP = [
		('white-uk', 'White - English/Welsh/Scottish/Northern Irish'),
		('white-irish', 'White - Irish'),
		('white-gypsy', 'White - Gypsy or Irish Traveller'),
		('white-other', 'White - Other'),
		('mixed-white/carib', 'Mixed - White and Black Caribbean'),
		('mixed-white/african', 'Mixed - White and Black African'),
		('mixed-white/asian', 'Mixed - White and Asian'),
		('mixed-other', ' Mixed - Other'),
		('asian-indian', 'Asian - Indian'),
		('asian-pakistani','Asian - Pakistani'),
		('asian-bangladeshi', 'Asian - Bangladeshi'),
		('asian-other', 'Asian - Other'),
		('black-african','Black - African'),
		('black-carib','Black - Caribbean'),
		('black-other', 'Black - Other'),
		('other-arab', 'Other - Arab'),
		('other-other','Other - Any other ethnic group')
	]

	#user = User.objects.get(user='username')
	age_range = models.CharField(max_length= 40, choices= AGE_RANGE, blank=False)
	gender = models.CharField(max_length= 12, choices = GENDER, blank=False)
	ethnic_group= models.CharField(max_length=100, choices=ETHNIC_GROUP, blank=False)
	favourite_genre= models.CharField(max_length=100, choices=MUSIC_GENRE, blank=False)
	artists_you_listen_to= models.TextField(blank=False)
	favourite_hangout_spots= models.TextField(blank=False)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	#ßclass models.User(models.Model):








