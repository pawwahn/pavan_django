from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('app_name',views.app_name,name='app_name')
]
