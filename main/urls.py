from django.urls import re_path
from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view),
    url(r'^register$', views.register_view, name='register'),

]