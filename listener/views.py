from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ListenerQuestionnaireForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from register.forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def listenerquestionnaire_view(request):
	user=request.user
	if request.method == "POST":
		listenerquestionnaire_form = ListenerQuestionnaireForm(request.POST)
		if listenerquestionnaire_form.is_valid():
				listenerquestionnaire_form.save()
		return redirect("success")
	else:
		listenerquestionnaire_form =ListenerQuestionnaireForm(request.POST)
		

	return render(request, "listenerquestionnaire.html", {"listenerquestionnaire_form": listenerquestionnaire_form})