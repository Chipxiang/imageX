from django.conf.urls import url
from . import views

app_name = "account"
urlpatterns = [

    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'register/$', views.user_register,name='register'),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    #url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),




]


