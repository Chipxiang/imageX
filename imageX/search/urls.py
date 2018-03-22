from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'$', views.results, name='results'),
    re_path(r'', views.index, name="index"),

]