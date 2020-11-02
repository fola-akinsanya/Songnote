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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path
from pages.views import homepage_view, musician_home_view, listener_home_view, leaderboard_view, feedback_view, questionnairesuccess_view, questionnairesuccess_view, successful_upload_view
from Profile.views import profile_detail_view
from register.views import register_view, profile_view, edit_profile_view, change_password_view
from django.urls import path, include
from listener.views import listenerquestionnaire_view, listenerfeedback_view
from musician.views import upload_song_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', homepage_view, name='home'),
    path('musician_home', musician_home_view, name='musician_home'),
    path('listener_home', listener_home_view, name='listener_home'),
    path('leaderboard', leaderboard_view, name='leaderboard'),
    path('profile', profile_detail_view, name="profile"),
    path('upload_song',upload_song_view,name='upload'),
    path("register", register_view, name="register"),
    path("register-2", profile_view, name="register-2"),
    path('edit_profile', edit_profile_view, name='edit_profile'),
    path('questionnaire', listenerquestionnaire_view, name='questionnaire'),
    path('success', questionnairesuccess_view,name='success'),
    path('feedback', listenerfeedback_view, name='feedback'),
    path('upload_success', successful_upload_view, name='upload success'),
    path('change_password',change_password_view, name='change_password'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset_choose_password.html'), name='password_reset_confirm'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

    url(r'^admin/',(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



















