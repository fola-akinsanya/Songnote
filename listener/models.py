from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.conf import settings


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

	added_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	age_range = models.CharField(max_length= 40, choices= AGE_RANGE)
	gender = models.CharField(max_length= 12, choices = GENDER)
	ethnic_group= models.CharField(max_length=100, choices=ETHNIC_GROUP)
	favourite_genre= models.CharField(max_length=100, choices=MUSIC_GENRE)
	artists_you_listen_to= models.TextField()
	favourite_hangout_spots= models.TextField()
	
class ListenerFeedback(models.Model):
	PLAYLIST = [
	('yes', 'Yes'),
	('no', 'No')
	]

	PRODUCTION_VALUE = [
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5')
	]

	LYRIC_VALUE = [
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5')
	]

	VOCAL_PERF= [
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5')
	]
		
	LISTEN_AGAIN = [
	('yes', 'Yes'),
	('no', 'No')
	]

	LISTEN_ANOTHER = [
	('yes', 'Yes'),
	('no', 'No')
	]

	WATCH_LIVE = [
	('yes', 'Yes'),
	('no', 'No')
	]

	HIT = [
	('yes', 'Yes'),
	('no', 'No')
	]

	added_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
	playlist= models.CharField(max_length= 12, choices = PLAYLIST)
	production_value= models.CharField(max_length= 12, choices = PRODUCTION_VALUE)
	lyrical_value= models.CharField(max_length= 12, choices = LYRIC_VALUE)
	vocal_perf= models.CharField(max_length= 12, choices = VOCAL_PERF)
	listen_again= models.CharField(max_length= 12, choices = LISTEN_AGAIN)
	listen_another= models.CharField(max_length= 12, choices = LISTEN_ANOTHER)
	watch_live = models.CharField(max_length= 12, choices = WATCH_LIVE)
	hit = models.CharField(max_length= 12, choices = HIT)
	





































