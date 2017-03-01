from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import JsonResponse
from connections import MySQLConnection
from models import Movie
import requests


class GetMovieList(TemplateView):
    
    def get_movie_name(self, query):
        result = Movie.objects.filter(name__istartswith=query)
        return list(set([title.name for title in result]))
    
    def get(self, request, **kwargs):
        query_params = request.GET
        query_term = query_params.get('q')
        movie_info = self.get_movie_name(query_term)
        return JsonResponse({'movie': movie_info[:7]}, status=200)
        
        
class HomePage(TemplateView):
    
    def get(self, request, **kwargs):
        return render(request, 'index.html')
        
        
class GetMovieCoordinates(TemplateView):
    
    def get_movie_location(self, query):
        if not query:
            return list()
        result = Movie.objects.filter(name__istartswith=query)
        return list(set([title.location + 'san francisco' for title in result]))
    
    def get_location_coordinates(self, location_list):
        location_info = dict()
        for location in location_list:
            url = 'https://maps.googleapis.com/maps/api/geocode/json'
            API_KEY = 'AIzaSyB_ZqeODAzV1alPXdBthhehVIgphYHXVOs'
            response = requests.get(url, params={'address': location, 'key': API_KEY})
            if response.json().get('results'):
                location_coordinates = response.json().get('results')[0].get('geometry').get('location')
                location_info[location] = location_coordinates
        return location_info
        
    def get(self, request, **kwargs):
        query_params = request.GET
        query_term = query_params.get('search-value')
        location_list = self.get_movie_location(query_term)
        if not location_list:
            return redirect('homepage')
        # coordinates_dict = self.get_location_coordinates(location_list)
        return render(request, 'location.html', {'location_list': '|'.join(location_list), 'search_value':query_term })