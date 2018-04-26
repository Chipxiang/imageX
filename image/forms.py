from .models import Image
from .models import Tag
from .models import Category
from django import forms
from django.forms import formset_factory


class ImageForm(forms.ModelForm):
    title = forms.CharField(required=False)
    description = forms.CharField(widget= forms.Textarea,required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False,help_text="Select the category the image belongs to (if any)")
    class Meta:
        model = Image
        fields = ('title','description','category','image')


class TagForm(forms.Form):
	word = forms.CharField(max_length=100)
