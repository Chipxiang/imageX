from django.db import models
from datetime import datetime
import django.contrib.auth.models as auth_models

class Member( auth_models.User):
    name = models.CharField(max_length=50)
    #image = models.ImageField()
    upload_quota = models.IntegerField(default=4)
    image_quota = models.IntegerField(default=3)
    #address = models.EmailField()
    def __str__(self):
        return self.username
