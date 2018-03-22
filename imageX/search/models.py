from django.db import models


class Member(models.Model):
    member_name = models.CharField(max_length=50)

    def __str__(self):
        return self.member_name


class Image(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    image_tag = models.CharField(max_length=200)
    image_category = models.CharField(max_length=50)
    def __str__(self):
        return self.image_tag


