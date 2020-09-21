from django.contrib import admin
from .models import SongUpload
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Register your models here.

class SongUploadAdmin(admin.ModelAdmin):
	list_display = ('artist','title','song_genre','song',)
 
admin.site.register(SongUpload,SongUploadAdmin)
