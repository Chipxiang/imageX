from django.urls import re_path
from django.conf.urls import url
from . import views

app_name = 'image'

urlpatterns = [
    url(r'^$', views.image_list, name="list"),
    url(r'upload/', views.upload, name="upload"),
    #url(r'view/(?P<filename>.*)/', views.image_detail, name='detail'),
    url(r'^detail/(?P<filename>.*)/', views.image_detail, name='detail'),
    url(r'^like/$', views.image_like, name='like'),

]