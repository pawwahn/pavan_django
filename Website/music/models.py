from django.db import models

# Create your models here.
# After creating or updating anything in this file, make sure you python manage.py makemigrations and migrate

class Album(models.Model):
    artist = models.CharField(max_length = 60)
    album_title = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 150)
    album_logo = models.CharField(max_length = 1000)

    def __str__(self):
        return self.artist+ " "+self.album_title + " "+self.genre+" "+self.album_logo

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length = 10)
    song_title = models.CharField(max_length = 250)

    def __str__(self):
        return self.song_title



