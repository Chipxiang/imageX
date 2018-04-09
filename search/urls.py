from django.urls import re_path
from . import views
from django.conf.urls import url

app_name = "search"
urlpatterns = [
    url(r'', views.search, name='search'),
]