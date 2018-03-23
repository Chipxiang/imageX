from django import forms
from upload.models import Image

class SearchForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'tag', 'image')