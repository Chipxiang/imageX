from django.http import HttpResponse
from django.shortcuts import render
from upload.models import Image
from .forms import SearchForm

def index(request):

    return render(request, 'search/searchBytags.html')


def results(request):
    keyword = request.GET['searchItem']
    list_images = Image.objects.all()
    context = {'list_images': list_images, 'keyword': keyword}
    return render(request, 'search/result.html',context)


