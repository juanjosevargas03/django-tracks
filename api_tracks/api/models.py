from django.db import models

# Create your models here.

class Genre(models.Model):
    genreId = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)



class Track(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    artistName = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    releaseDate = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    artistId = models.CharField(max_length=50)
    artistUrl = models.CharField(max_length=100)
    contentAdvisoryRating = models.CharField(max_length=100)
    artworkUrl100 = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre,related_name='genres')    
    url = models.CharField(max_length=100)
    



