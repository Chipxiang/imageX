from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image
from account.models import Member
from django.urls import reverse
from django.http import HttpResponseRedirect

@login_required
def upload(request):

    member = Member.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            description = form.cleaned_data['description']
            tag = form.cleaned_data['tag']
            #image = ImageForm.clean_image()
            image = form.cleaned_data['image']
            #category = form.cleaned_data['category']
            u = Image()
            u.tag = tag
            u.description = description
            #u.category = category

            u.image = image
            if( member ):
                u.owner = member
            u.save()
            return HttpResponseRedirect(reverse("account:dashboard"))
    else:
        form = ImageForm()
    return render(request, 'ImageManagement/model_form_upload.html', {'form': form ,'username': request.user.username} )

# def list(request):
