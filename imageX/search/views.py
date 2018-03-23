from django.http import HttpResponse
from django.shortcuts import render
from main.models import Image
from .forms import SearchForm

'''
def index(request):

     return render(request, 'search/searchBytags.html')


def results(request):
    keyword = request.GET['searchItem']
    list_images = Image.objects.all()
    context = {'list_images': list_images, 'keyword': keyword}
    return render(request, 'search/result.html',context)
'''

def searchImage(request):
    list_images = []
    base_images = Image.objects.order_by('uploaded_at')
    nothing = False
    if 'searchItem' in request.GET:
        keyword = request.GET['searchItem']
        list_images = Image.objects.filter(title=keyword)
        if not list_images:
            nothing = True

    context = {'list_images': list_images, 'base_images': base_images, 'nothing': nothing}
    return render(request, 'search/searchByTags.html', context)

