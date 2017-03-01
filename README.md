# Movie Location Finder Django App

### What purpose does it solve

An application that helps in finding all the locations on the map where a movie is currently playing.
A search bar is provided to search for a movie and also the autocomplete feature is applied on the 
search terms.

### Running instance available at
https://feature-autocomplete-dormamu.c9users.io/

Setup local mysql server and provide the credentials in feature_autocomplete/settings.py
Look for the *DATABASES* field in the file and update it.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'maindb',
        'USER': 'dormamu',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

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

Populate the db with data from xml file *data.xml*
```
python manage.py makemigrations
python manage.py migrate
python populate_db.py
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
