from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Song

# Create your views here.
def index(request):
    albums = Album.objects.all()
    html =''
    for album in albums:
        url =  str(album.id) +'/'
        html+= ' <a href="'+ url +'">' + album.album_title + '</a><br>'
    return HttpResponse(html)

def app_name(request):
    return HttpResponse("<h1>This is Music App")

def detail(request, alb_id):
    return HttpResponse("<h1>The Details of album : " +str(alb_id) + " are below </h1>")
