from main.models import Image
from django import forms


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'tag', 'image')
