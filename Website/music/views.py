from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album, Song


# Create your views here.
# def index(request):
#     albums = Album.objects.all()
#     html =''
#     for album in albums:
#         url =  str(album.id) +'/'
#         html+= ' <a href="'+ url +'">' + album.album_title + '</a><br>'
#     return HttpResponse(html)


# def index(request):
#     # getting values from db
#     all_albums = Album.objects.all()
#
#     # create a folder under music>templates>music> and create ur html files here
#     # with the help of loader.get_template() , django understands from whr to get the file..
#
#     #create a dictonary(which can be with any name(preferable 'context'))
#     context = {'all_albums':all_albums}
#
#     template = loader.get_template('music/index.html')
#     return HttpResponse(template.render(context, request)) # template.render(dict, request) -- every view return something.. # can be done like this and also we have other way..



def index(request):
    # getting values from db
    all_albums = Album.objects.all()
    # create a folder under music>templates>music> and create ur html files here

    #create a dictonary(which can be with any name(preferable 'context'))
    context = {'all_albums':all_albums}
    return render(request, 'music/index.html',context)


def app_name(request):
    return HttpResponse("<h1>This is Music App")

# def detail(request, alb_id):
#     return HttpResponse("<h1>The Details of album : " +str(alb_id) + " are below </h1>")

def detail(request, alb_id):
    try:
        album = Album.objects.get(pk=alb_id)
        context = {'album':album}
    except Album.DoesNotExist:
        raise Http404("Album Does Not Exist")
    return render(request, 'music/detail.html', context)
