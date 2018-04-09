from django.shortcuts import render
from django.http import HttpResponse
from image.models import Image
from .forms import SearchForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib import messages
'''
def search(request):

    limit = 2
    list_images = []
    base_images = Image.objects.order_by('-uploaded_at')
    searchAction = False
    p=Paginator(base_images, limit)
    page = request.GET.get('page')
    try:
        base_images = p.page(page)
    except PageNotAnInteger:
        base_images = p.page(1)
    except EmptyPage:
        base_images = p.page(paginator.num_pages)

    if 'searchItem' in request.GET:
        keyword = request.GET['searchItem']
        if keyword != None :

           list_images = Image.objects.filter(tag__icontains=keyword).order_by('-uploaded_at')
           if not list_images:
              searchAction = True
           paginator = Paginator(list_images, limit)
           page = request.GET.get('page')

           try:
             list_images = paginator.page(page)
           except PageNotAnInteger:
             list_images = paginator.page(1)
           except EmptyPage:
             list_images = paginator.page(paginator.num_pages)
        else:
            searchAction = False

    context = {'list_images':list_images, 'base_images':base_images,'searchAction':searchAction, 'section': 'search'}

    return render(request, 'search/search.html', context)
'''
def search(request):
    images = Image.objects.all()

    if 'searchItem' in request.GET:
        keyword = request.GET['searchItem']
        if keyword != None :
           images = Image.objects.filter(tag__icontains=keyword).order_by('-uploaded_at')
           if not images:
               messages.error(request, 'No image matches your request')

    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range return an empty page
            return HttpResponse('')
        # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'image/list_ajax.html',
                      {'section': 'search', 'images': images,})
    return render(request,
                  'image/list_new.html',
                  {'section': 'search', 'images': images,})


