from django.contrib import admin

# Register your models here.
from music.models import Album  # The Class name or model name
from music.models import Song

admin.site.register(Album)
admin.site.register(Song)

