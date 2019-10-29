"""
Definition of urls for DjangoFinalProject2019.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('samples/', views.samples, name='samples'),
    path('secret', views.secret, name='secret'),
    path('info', views.info, name='info'),
    path(r'^holiday/(?P<message>[A-Za-z\s\d*\W]+)$', views.holiday, name='holiday'),
    path('episodes/<season_num>', views.episodes, name='episodes'),
    path('episode_details/<season_num>/<ep_num>', views.episodeDetails, name='episodeDetails'),
    path('add_episode_to_watch/<name>/<id>', views.add_episode_to_watch, name='add_episode_to_watch'),
    path('about/', views.about, name='about'),
]