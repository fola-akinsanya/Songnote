from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ListenerQuestionnaireForm, ListenerFeedbackForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from register.forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def listenerquestionnaire_view(request):
	if request.method == "POST":
		listenerquestionnaire_form = ListenerQuestionnaireForm(request.POST)
		if listenerquestionnaire_form.is_valid():
				listenerquestionnaire_form.save()
		return redirect("success")
	else:
		listenerquestionnaire_form =ListenerQuestionnaireForm()
		

	return render(request, "listenerquestionnaire.html", {"listenerquestionnaire_form": listenerquestionnaire_form})

@login_required
def listenerfeedback_view(request):
	if request.method == "POST":
		listenerfeedback_form = ListenerFeedbackForm(request.POST)
		if listenerfeedback_form.is_valid():
				listenerfeedback_form.save()
		return redirect("success")
	else:
		listenerfeedback_form =ListenerFeedbackForm()
		

	return render(request, "listenerfeedback.html", {"listenerfeedback_form": listenerfeedback_form})
