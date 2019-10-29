
from django.http import HttpRequest
import requests
import datetime
import json


class fetch():
    
    def fetch_season_info():

        '''
            What we want from our response:
            still_path - for our image
            season_number - duh
            episode_count - shows the # of eps in season
            overview - brief desc
            air_date - the year of season
        '''

        api_key = "d194eb72915bc79fac2eb1a70a71ddd3"

        url = "https://api.themoviedb.org/3/tv/1402?api_key=" + api_key
        response = requests.get(url)
        stuff = []

        if(response.ok):
            jData = json.loads(response.content)
            data = jData['seasons']
            images = []
            for idx in range(len(data)):
                image = data[idx]['poster_path']
                images.append(image)

            stuff.append(images)
              
        else:
            jData = None

        return stuff

    def getEpisodes(season_num):
        '''
            What we want from our response:
            episode_number - duh
            name - name of the episode
            overview - brief desc
            still_path - episode image??
            and mucho more!
        '''
        
        api_key = "d194eb72915bc79fac2eb1a70a71ddd3"

        url = "https://api.themoviedb.org/3/tv/1402/season/" + season_num + "?api_key=" + api_key
        response = requests.get(url)
        stuff = []

        if(response.ok):
            jData = json.loads(response.content)
            data = jData['episodes']
            names = []
            overviews = []
            paths = []
            ep_nums = []
            for idx in range(len(data)):
                name = data[idx]['name']
                overview = data[idx]['overview']
                names.append(name)
                overviews.append(overview)
                path = data[idx]['still_path']
                paths.append("https://image.tmdb.org/t/p/original" + path)
                ep_num = data[idx]['episode_number']
                ep_nums.append(ep_num)

            stuff.append(names)
            stuff.append(overviews)
            stuff.append(paths)
            stuff.append(ep_nums)
            
        else:
            stuff = None

        return stuff

    
    def getEpisodeDetails(season_num, ep_num):

        # get episodes details 

        '''
            What we want from our response:
            name - name of the episode
            overview - brief desc
            still_path - episode image??
            crew - name, job, profile_path
            guest_stars - name, character, profile_path
        '''
        api_key = "d194eb72915bc79fac2eb1a70a71ddd3"

        url = "https://api.themoviedb.org/3/tv/1402/season/" + season_num + "/episode/" + ep_num + "?api_key=" + api_key
        response = requests.get(url)
        episodedetails = {} # dictionary for episode details

        if response.ok:
            jData = json.loads(response.content)
            episodedetails['name'] = jData['name']
            episodedetails['overview'] = jData['overview']
            episodedetails['still_path'] = "https://image.tmdb.org/t/p/original" + str(jData['still_path'])
            
            crew_list = [] # empty list for crew
            data = jData['crew']
            for idx in range(len(data)):
                crew = {} # dictionary for crew
                crew['name'] = data[idx]['name']
                crew['job'] = data[idx]['job']
                crew['profile_path'] = "https://image.tmdb.org/t/p/original" + str(data[idx]['profile_path'])
                
                crew_list.append(crew)

            episodedetails['crew_list'] = crew_list
            
            guest_stars = [] # empty list for guest stars
            data = jData['guest_stars']
            for idx in range(len(data)):
                guest_star = {}
                guest_star['name'] = data[idx]['name']
                guest_star['character'] = data[idx]['character']
                guest_star['profile_path'] = "https://image.tmdb.org/t/p/original" + str(data[idx]['profile_path'])

                guest_stars.append(guest_star)
            
            episodedetails['guest_stars'] = guest_stars

        else:
            episodedetails = None

        return episodedetails