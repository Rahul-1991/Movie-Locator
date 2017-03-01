from django.conf.urls import url
from autocomplete import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='homepage'),
    url(r'^movies/$', views.GetMovieList.as_view(), name='get-movie-list'),
    url(r'^movies/coordinates/$', views.GetMovieCoordinates.as_view(), name='get-movie-coordinates')
]
