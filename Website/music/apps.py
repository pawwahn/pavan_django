from django.apps import AppConfig

#every app you create should be mentioned in settings.py under INSTALLED_APPS as music.apps.MusicConfig

class MusicConfig(AppConfig):
    name = 'music'
