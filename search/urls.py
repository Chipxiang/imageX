from django.urls import re_path
from . import views
from django.conf.urls import url
urlpatterns = [

    url(r'', views.searchImage, name='searchImage'),

]