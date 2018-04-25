from .models import Image
from .models import Tag
from django import forms
from django.forms import formset_factory


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','description', 'category','image')


class TagForm(forms.Form):
	word = forms.CharField(max_length=100)
