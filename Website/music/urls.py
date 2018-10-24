from django.urls import path
from . import views

urlpatterns = [

    # /music/
    path('', views.index,name='index'),

    # /music/app_name
    path('app_name',views.app_name,name='app_name'),

    # /music/123/
    path('(?P<alb_id>[0-9]+)',views.details,name='details')
]
