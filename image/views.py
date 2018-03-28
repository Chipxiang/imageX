from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image
from account.models import Member
from django.urls import reverse
from django.http import HttpResponseRedirect , HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

@login_required
def upload(request):
    member = Member.objects.get(username=request.user.username)
    if( member.image_quota >0 and member.upload_quota >0):
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
              description = form.cleaned_data['description']
              tag = form.cleaned_data['tag']
              image = form.cleaned_data['image']
              category = form.cleaned_data['category']
              title = form.cleaned_data['title']
              u = Image(title=title, tag=tag,description=description,
                      category=category, image=image,owner=member)
              u.save()
              member.image_quota = member.image_quota - 1
              member.upload_quota = member.upload_quota - 1
              member.save()
              return HttpResponseRedirect(reverse("account:dashboard"))
        else:
          form = ImageForm()
        return render(request, 'image/model_form_upload.html', {'form': form ,'username': request.user.username} )
    else:
        return HttpResponse("no quota")

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

    return render(request, "image/list.html", {'list_images':list_images} )
