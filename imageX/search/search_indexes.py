import datetime
from haystack import indexes
from .models import Image


class ImageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    tag = indexes.CharField(model_attr='tag')
    owner = indexes.CharField(model_attr='owner')


    def get_model(self):
        return Image

    def index_queryset(self, using=None):
        return Image.objects.all()
