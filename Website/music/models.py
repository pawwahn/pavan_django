from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length = 60)
    album_title = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 150)
    album_logo = models.CharField(max_length = 1000)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length = 10)
    song_title = models.CharField(max_length = 250)

