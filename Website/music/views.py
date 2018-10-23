from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is 1st page")

def app_name(request):
    return HttpResponse("<h1>This is Music App")
