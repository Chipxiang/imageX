from django.urls import re_path
from . import views
from django.conf.urls import url
urlpatterns = [
    #re_path(r'$', views.results, name='results'),
    #re_path(r'', views.index, name='index')

    #url(r'results/', views.results, name='results'),
    url(r'', views.searchImage, name='searchImage'),

]