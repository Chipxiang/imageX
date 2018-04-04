from django.shortcuts import render
from django.http import HttpResponse
from image.models import Image
from .forms import SearchForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger




def searchImage(request):

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

    context = {'list_images':list_images, 'base_images':base_images,'searchAction':searchAction, }

    return render(request, 'search/search.html', context)


def viewImage(request , filename):

    return HttpResponse("hello")