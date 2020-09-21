from django.contrib import admin
from .models import ListenerQuestionnaire, ListenerFeedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Register your models here.


class ListenerQuestionnaireAdmin(admin.ModelAdmin):
	list_display = ('added_by','age_range', 'gender','ethnic_group','favourite_genre','artists_you_listen_to','favourite_hangout_spots')
	def save_user(self, request, obj, form, change):
		obj.added_by = request.user.username
		obj.added_by.save()
		return questionnaireform
 
admin.site.register(ListenerQuestionnaire, ListenerQuestionnaireAdmin)

class ListenerFeedbackAdmin(admin.ModelAdmin):
 
    def get_feedbackform(self, request, obj=None, **kwargs):
        feedbackform = super(ListenerFeedbackAdmin, self).get_feedbackform(request, obj, **kwargs)
        feedbackform.base_fields['added_by'].initial = request.user
        return feedbackform
 
admin.site.register(ListenerFeedback, ListenerFeedbackAdmin)




