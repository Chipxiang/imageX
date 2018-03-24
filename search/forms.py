from django import forms
from main.models import Image

class SearchForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('tag', 'image')