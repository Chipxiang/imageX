from django import forms
from image.models import Image

SearchType_CHOICES = [('Tag','tag'),('Photographer','photographer'),('Category','category')]
OrderType_CHOICES = [('Time','time'),('Popularity','popularity')]
class SearchForm(forms.Form):
     searchType = forms.ChoiceField(
        choices=SearchType_CHOICES,)
     orderType = forms.ChoiceField(
        choices=OrderType_CHOICES, )
     keyword = forms.CharField(label='search',widget=forms.TextInput(attrs={'placeholder': 'Search'}))

     def change(self,one,two,three):
        searchType = one;
        orderType = two;
        keyword = three;



     def save(self):
         searchType = self.cleaned_data["searchType"]
         orderType = self.cleaned_data["orderType"]
         keyword =  self.cleaned_data["keyword"]


    #class Meta:
       # model = Image
      #  fields = ('tag', 'image')