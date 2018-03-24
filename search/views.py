
from django.shortcuts import render
from main.models import Image
from .forms import SearchForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


def searchImage(request, Username=None):
    limit = 2
    list_images = []
    base_images = Image.objects.order_by('uploaded_at')
    nothing = False

    if 'searchItem' in request.GET:
        keyword = request.GET['searchItem']
        list_images = Image.objects.filter(tag=keyword)
        if not list_images:
            nothing = True
        paginator = Paginator(list_images, limit)
        page = request.GET.get('page')
        try:
           list_images = paginator.page(page)
        except PageNotAnInteger:
           list_images = paginator.page(1)
        except EmptyPage:
           list_images = paginator.page(paginator.num_pages)

    context = {'list_images':list_images, 'base_images':base_images,'nothing':nothing, }
    return render(request, 'search/searchByTags.html', context)


