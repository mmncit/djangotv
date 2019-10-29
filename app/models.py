"""
Definition of models.
"""

from django.db import models
from django import forms

# Watch Class
class Watch(models.Model):
    ep_name = models.CharField('Name', max_length=100)
    ep_id = models.PositiveIntegerField('EPid')
    season = models.PositiveIntegerField('season')
    poster_path = models.CharField('Poster', max_length=200)
    overview = models.CharField('Overview', max_length=300)

# Watch Form
class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ['ep_name', 'ep_id', 'season', 'poster_path', 'overview']