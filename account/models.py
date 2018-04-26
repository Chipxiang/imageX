from django.db import models
from datetime import datetime
import django.contrib.auth.models as auth_models
from django.conf import settings
from django.core.validators import FileExtensionValidator


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user/{0}_{1}'.format(instance.user.username, filename)

class Member( auth_models.User):
    upload_quota = models.IntegerField(default=100)
    image_quota = models.IntegerField(default=200)
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(default=None,max_length=50)
    self_description = models.TextField(default='',max_length=500)
    avatar = models.ImageField(upload_to=user_directory_path,validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg'])],default="media/default/avatar.jpg")
    def __str__(self):

        return self.user.username