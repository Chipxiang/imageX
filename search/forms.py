from django import forms
from image.models import Image

SearchType_CHOICES = [('Tag','tag'),('Photographer','photographer'),('Gallery','gallery')]
OrderType_CHOICES = [('Time','time'),('Popularity','popularity')]
class SearchForm(forms.Form):
     searchType = forms.ChoiceField(
        choices=SearchType_CHOICES,)
     orderType = forms.ChoiceField(
        choices=OrderType_CHOICES, )
     keyword = forms.CharField()


     def save(self):
         searchType = self.cleaned_data["searchType"]
         orderType = self.cleaned_data["orderType"]
         keyword =  self.cleaned_data["keyword"]


    #class Meta:
       # model = Image
      #  fields = ('tag', 'image')