from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.TextField(default=None, blank=True, null=True)
    location = models.TextField(default=None, blank=True, null=True)
    
    class Meta:
        db_table = 'movie_location'
