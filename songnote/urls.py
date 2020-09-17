"""songnote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import homepage_view, musician_home_view, listener_home_view, leaderboard_view, feedback_view, uploaded_songs_view, questionnairesuccess_view, questionnairesuccess_view
from Profile.views import profile_detail_view
from register.views import register_view, profile_view
from django.urls import path, include
from listener.views import listenerquestionnaire_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', homepage_view, name='home'),
    path('musician_home', musician_home_view, name='musician_home'),
    path('listener_home', listener_home_view, name='listener_home'),
    path('leaderboard', leaderboard_view, name='leaderboard'),
    path('profile', profile_detail_view),
    path('feedback',feedback_view),
    path('uploaded_songs',uploaded_songs_view),
    path("register", register_view, name="register"),
    path("register-2", profile_view, name="register-2"),
    path('questionnaire', listenerquestionnaire_view, name='questionnaire'),
    path('success', questionnairesuccess_view,name='success')

]
