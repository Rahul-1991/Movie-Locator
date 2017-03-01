# Movie Location Finder

### What purpose does it solve

An application that helps in finding all the locations on the map where a movie is currently playing.
A search bar is provided to search for a movie and also the autocomplete feature is applied on the 
search terms.

Creating the environment
```
virtualenv venv
```

Activating environment
```
source venv/bin/activate
```
Installing dependencies
```
pip install -r requirements.txt
```

Running the server

```
python manage.py runserver
```

### APIs

#### Autocomplete
An api which takes a string and returns a list of strings 
having the input string as its prefix. The lookup is performed 
in the mysql table.

#### GetLocation
An api which takes the movie name as input and return the list of
coordinates for the places where the movie is currently playing. 


### External Libraries

#### Google Maps
The Google maps API is used to render the map for displaying the location.

#### Google GeoLocation API
This API is used to get the map coordinates for a given location.

### Endpoints
