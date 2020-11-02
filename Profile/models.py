from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
	USER_TYPE_CHOICES = [
		('musician', 'Musician'),
		('listener', 'Listener'),
	]

	Name = models.TextField()
	User_type = models.CharField(max_length= 12, choices = USER_TYPE_CHOICES)

