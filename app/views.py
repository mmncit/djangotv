"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app import fetch
from app import models
import json


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    stuff = fetch.fetch.fetch_season_info()
    images = stuff[0]

    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'images': images,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def samples(request):
    """Renders the samples page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/samples.html',
        {
            'title':'Samples',
            'message':'Your samples page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def secret(request):
    assert isinstance(request, HttpRequest)
    
    secret = request.GET.get('secret')
    return render(
        request,
        'app/samples.html',
        {
            'title': 'Your Team',
            'message': 'Your application description page.',
            'year': datetime.now().year,
            'secret': secret,
        }
    )


def holiday(request):
    assert isinstance(request, HttpRequest)
    
    message = request.GET.get('message')
    return render(
        request,
        'app/samples.html',
        {
            'title': 'Your Team',
            'message': 'Your application description page.',
            'year': datetime.now().year,
            'secret': secret,
        }
    )


def info(request):
    assert isinstance(request, HttpRequest)
    
    country = request.POST.get('country')
    return render(
        request,
        'app/samples.html',
        {
            'title': 'Your Country',
            'message': 'Your application description page.',
            'year': datetime.now().year,
            'country': country,
        }
    )

def episodes(request, season_num):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    
    stuff = fetch.fetch.getEpisodes(season_num)
    names = stuff[0]
    overviews = stuff[1]
    paths = stuff[2]
    ep_nums = stuff[3]
    
    return render(
        request,
        'app/episodes.html',
        {
            'title': 'Episodes',
            'message': 'Your application description page.',
            'year': datetime.now().year,
            'ep_details': zip(names, overviews, paths, ep_nums),
            'season_num': season_num,
        }
    )

def episodeDetails(request, season_num, ep_num):
    """Renders the episode details page."""
    assert isinstance(request, HttpRequest)
    
    episodedetails = fetch.fetch.getEpisodeDetails(season_num, ep_num)
    name = episodedetails['name']
    overview = episodedetails['overview']
    still_path = episodedetails['still_path']

    # for crew
    crew_list = episodedetails['crew_list']
    crew_names = [ dict['name'] for dict in crew_list ]
    crew_jobs = [ dict['job'] for dict in crew_list ]
    crew_profile_paths = [ dict['profile_path'] for dict in crew_list ]
    
    # for cast
    star_list = episodedetails['guest_stars']
    star_names = [ dict['name'] for dict in star_list ]
    star_characters = [ dict['character'] for dict in star_list ]
    star_profile_paths = [ dict['profile_path'] for dict in star_list ]

    return render(
        request,
        'app/episode_details.html',
        {
            'title': 'Episode Details',
            'message': 'Your application description page.',
            'year': datetime.now().year,
            'season_num': str(season_num),
            'ep_num' : str(ep_num),
            'name' : name,
            'path' : still_path,
            'overview': overview,
            'crew_info': zip(crew_names, crew_jobs, crew_profile_paths),
            'star_info': zip(star_names, star_characters, star_profile_paths),
        }
    )

def add_episode_to_watch(request, name, id):                   ### add to watch ###
    #form = WatchForm(request.POST)
    #form.save()
    return HttpResponseRedirect('/')