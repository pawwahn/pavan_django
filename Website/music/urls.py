from django.urls import path
from . import views
from django.urls import re_path  # for higher versions..

urlpatterns = [

    # /music/
    path('', views.index,name='index'),

    # /music/app_name
    path('app_name',views.app_name,name='app_name'),


    # for lower versions of django 2.0, its re to be used..
    # for higher versions of django 2.2 and above, it should be used as re_path

    # /music/123/

    re_path('(?P<alb_id>[0-9]+)',views.detail,name='detail')    # this also works..
    #path(r'^[0-9]$',views.detail,name='detail')
    #re_path('<alb_id>(\d+)/', views.detail, name='detail')
    #path('<str:alb_id>', views.detail, name='detail')  # /music/71/
    #re_path(r'^(?P<alb_id>[0-9]+)/$', views.detail, name='detail') # this also works..

]
