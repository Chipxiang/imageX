from django.db import models
from django.utils import timezone
from account.models import Member
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.core.validators import FileExtensionValidator

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}_{1}'.format(instance.title, filename)

class Category(models.Model):
    text = models.CharField(max_length=20)
    def __str__(self):
        return self.text


class Image(models.Model):
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=20)
    tag = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to=user_directory_path,validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg'])])
    uploaded_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.tag: self.tag = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('image:detail', args=[self.image])