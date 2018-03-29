from django.urls import re_path
from . import views

app_name = 'image'

urlpatterns = [
    re_path(r'^$', views.list, name="list"),
    re_path(r'upload/', views.upload, name="upload"),
    re_path(r'view/(?P<filename>.*)/', views.view,name='view'),

]