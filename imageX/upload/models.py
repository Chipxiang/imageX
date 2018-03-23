from django.db import models
from django.utils import timezone

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'image_{0}/{1}'.format(instance.owner, filename)

class Member(models.Model):
    member_name = models.CharField(max_length=50, default=None)
    def __str__(self):
        return self.member_name

class Category(models.Model):
    text = models.CharField(max_length=20)

class Image(models.Model):
    image_id = models.CharField(max_length=10)
    owner = 'Member000'
    #owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    tag = models.CharField(max_length=50)
    image = models.ImageField(upload_to=user_directory_path, default='media/no_image.jpg')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title