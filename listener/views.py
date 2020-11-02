from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ListenerQuestionnaireForm, ListenerFeedbackForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from register.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import ListenerQuestionnaire, ListenerFeedback, Song

# Create your views here.
@login_required
def listenerquestionnaire_view(request):
	if request.method == "POST":
		listenerquestionnaire_form = ListenerQuestionnaireForm(request.POST, added_by=request.user)
		if listenerquestionnaire_form.is_valid():
			listenerquestionnaire_form.save()
		return redirect("success")
	else:
		listenerquestionnaire_form =ListenerQuestionnaireForm()

	return render(request, "listenerquestionnaire.html", {"listenerquestionnaire_form": listenerquestionnaire_form})

@login_required
def listenerfeedback_view(request):
	songs = Song.objects.filter(reviewer=request.user)
	context = {
		'songs': songs,
		'listenerfeedback_form': ListenerFeedbackForm()
	}
	if request.method == "POST":
		listenerfeedback_form = ListenerFeedbackForm(request.POST, added_by=request.user)
		if listenerfeedback_form.is_valid():
				listenerfeedback_form.save()
		return redirect("success")
	else:
		listenerfeedback_form =ListenerFeedbackForm()

	return render(request, "listenerfeedback.html", context)
