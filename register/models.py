from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

	USER_TYPE_CHOICES = [
		('musician', 'Musician'),
		('listener', 'Listener'),
	]
	CITY_CHOICES = [
	('bath', 'Bath'),
	('birmingham','Birmingham'),
	('bradford','Bradford'),
	('brighton & hove', "Brighton & Hove"),
	('bristol', 'Bristol'),
	('cambridge', 'Cambridge'),
	('canterbury', 'Canterbury'),
	('carlisle','Carlisle'),
	('chester', 'Chester'),
	('chichester','Chichester'),
	('coventry','Coventry'),
	('derby','Derby'),
	('durham','Durham'),
	('ely','Ely'),
	('exeter', 'Exeter'),
	('gloucester','Gloucester'),
	('Hereford','Hereford'),
	('kingston upon Hull','Kingston upon Hull'),
	('lancaster', 'Lancaster'),
	('leeds','Leeds'),
	('leicester', 'Leicester'),
	('lichfield','Lichfield'),
	('lincoln','Lincoln'),
	('liverpool','Liverpool'),
	('london', 'London'),
	('manchester','Manchester'),
	('newcastle upon tyne', 'Newcastle upon Tyne'),
	('norwich', 'Norwich'),
	('nottingham','Nottingham'),
	('oxford', 'Oxford'),
	('peterborough', 'Peterborough'), 
	('plymouth','Plymouth'),
	('portsmouth', 'Portsmouth'),
	('preston', 'Preston'),
	('ripon', 'Ripon'),
	('salford','Salford'),
	('salisbury','Salisbury'),
	('sheffield', 'Sheffield'), 
	('southampton','Southampton'),
	('st albans','St Albans'), 
	('stoke-on-trent','Stoke-on-Trent'),
	('sunderland','Sunderland'), 
	('truro','Truro'),
	('wakefield','Wakefield'),
	('wells','Wells'),
	('westminster','Westminster'),
	('winchester', 'Winchester'),
	('wolverhampton', 'Wolverhampton'),
	('worcester','Worcester'),
	('york', 'York'),
	]
	user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	User_type = models.CharField(max_length= 12, choices = USER_TYPE_CHOICES)
	city_of_residence = models.CharField(max_length= 30, choices = CITY_CHOICES)

