from django.urls import re_path
from . import views
from django.conf.urls import url

app_name = "search"
urlpatterns = [

    url(r'', views.searchImage, name='searchImage'),
   # url(r'^(?P<filename>.*)', views.viewImage, name="viewImage"),

]