from django.contrib import admin
from .models import ListenerQuestionnaire, ListenerFeedback, Song
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Register your models here.


class ListenerQuestionnaireAdmin(admin.ModelAdmin):
	list_display = ('added_by','age_range', 'gender','ethnic_group','favourite_genre','artists_you_listen_to','favourite_hangout_spots')
	
 
admin.site.register(ListenerQuestionnaire, ListenerQuestionnaireAdmin)

class ListenerFeedbackAdmin(admin.ModelAdmin):
	list_display = ('added_by','playlist', 'production_value','lyrical_value','vocal_perf','listen_again','listen_another', 'watch_live','hit')

 
admin.site.register(ListenerFeedback, ListenerFeedbackAdmin)

class SongAdmin(admin.ModelAdmin):
	list_display = ('reviewer', 'song')

admin.site.register(Song,SongAdmin)





