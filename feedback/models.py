from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Leaderboard(models.Model):
	RANK = [
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
	('6','6'),
	('7','7'),
	('8','8'),
	('9','9'),
	('10','10')]

	ranking = models.CharField(max_length= 12, choices = RANK)
	listener = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)

