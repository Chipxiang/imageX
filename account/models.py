from django.db import models
import django.contrib.auth.models as auth_models

class Member( auth_models.User):
    #username = models.CharField(max_length=50)
    #password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    #address = models.EmailField()
    def __str__(self):
        return self.username
