from django.http import HttpResponse
from django.shortcuts import render
from upload.models import Image

def index(request):
    return render(request, 'search/index.html')

def details(request):
    return HttpResponse("hello world")

def results(request):
    keyword = request.GET['searchItem']
    list_images = Image.objects.all()
    context = {'list_images': list_images, 'keyword': keyword}
    return render(request, 'search/result.html', context)


