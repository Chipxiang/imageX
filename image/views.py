from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import ImageForm
from .forms import TagForm
from .models import Image
from .models import Tag
from account.models import Member
from django.urls import reverse
from django.http import HttpResponseRedirect , HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.forms.formsets import formset_factory
from django.contrib import messages

@login_required
def upload(request):
    member = Member.objects.get(username=request.user.username)
    TagFormSet = formset_factory(TagForm)
    if( member.image_quota >0 and member.upload_quota >0):
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            tag_formset = TagFormSet(request.POST or None)
            if form.is_valid():
              description = form.cleaned_data['description']
              image = form.cleaned_data['image']
              category = form.cleaned_data['category']
              title = form.cleaned_data['title']
              u = Image(title=title,description=description,
                      category=category, image=image,owner=member)
              u.save()
              if tag_formset.is_valid():
                for tag_form in tag_formset:
                  words = tag_form.cleaned_data.get('word')
                  if words is not None:
                    if not Tag.objects.filter(word=words):
                      t = Tag(word=words)
                      t.save()
                      u.tag.add(t)
                      u.save()
                    else:
                      t = Tag.objects.filter(word=words)[0]
                      u.tag.add(t)
                      u.save()
              member.image_quota = member.image_quota - 1
              member.upload_quota = member.upload_quota - 1
              member.save()


              return HttpResponseRedirect(reverse("account:dashboard"))
        else:
          form = ImageForm()
          tag_formset = TagFormSet()
        return render(request, 'image/model_form_upload.html', {'form': form ,'username': request.user.username, 'tag_formset':tag_formset} )
    else:
        return HttpResponse("no quota")
'''
@login_required
def list(request):
    limit = 10
    member=Member.objects.get(username=request.user.username)
    list_images = Image.objects.filter(owner=member).order_by('-uploaded_at')
    if(list_images):
       paginator = Paginator(list_images, limit)
       page = request.GET.get('page')

       try:
          list_images = paginator.page(page)
       except PageNotAnInteger:
          list_images = paginator.page(1)
       except EmptyPage:
          list_images = paginator.page(paginator.num_pages)

    return render(request, "image/list.html", {'list_images':list_images,'section': 'images'})
'''
#def view(request , filename):
    #image = Image.objects.get(image=filename)
    #return render(request , "image/view.html",{'image':image} )

@login_required
@require_POST
def image_like(request):
    image_name = request.POST.get('filename')
    action = request.POST.get('action')

    if image_name and action:
        try:
            image = Image.objects.get(image=image_name)
            if action == 'like':
               image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

def image_download(request, filename):
    image = get_object_or_404(Image, image=filename)
    image.download_count += 1
    image.save()
    messages.success(request, "Download Successfully")
    return redirect('image:detail', filename=image.image)

def image_delete(request,filename):
    delete = "delete"
    if(filename != "None"):
        member = Member.objects.get(username=request.user.username)
        image = get_object_or_404(Image, image=filename)
        image.delete()
        messages.success(request, " image deleted! ")
        delete = "delete"
        member.image_quota += 1
        member.save()


    member = Member.objects.get(username=request.user.username)
    images = Image.objects.filter(owner=member).order_by('-uploaded_at')
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
                      {'section': 'images', 'images': images,'delete': delete})
    return render(request,
                  'image/list_new.html',
                  {'section': 'images', 'images': images,'delete': delete})



def image_detail(request, filename ):
    image = get_object_or_404(Image, image=filename)
    return render(request, 'image/detail.html', {'section': 'images','image': image})

@login_required

def image_list(request):

    delete = "None"
    member = Member.objects.get(username=request.user.username)
    images = Image.objects.filter(owner=member).order_by('-uploaded_at')
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
                      {'section': 'images', 'images': images,'delete':delete})
    return render(request,
                  'image/list_new.html',
                   {'section': 'images', 'images': images,'delete': delete})


