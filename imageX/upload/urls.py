from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'', views.model_form_upload, name="upload"),
]