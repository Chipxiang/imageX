from django.db import models
from django.utils import timezone
from account.models import Member
from django.core.validators import FileExtensionValidator

def user_directory_path(instance):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}_{1}'.format(instance.title, instance.tag)

class Category(models.Model):
    text = models.CharField(max_length=20)
    def __str__(self):
        return self.text


class Image(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=20)
    tag = models.CharField(max_length=50)
    image = models.ImageField(upload_to=user_directory_path,validators=[FileExtensionValidator(allowed_extensions=['jpeg'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title