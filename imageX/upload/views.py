from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image

def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            tag = form.cleaned_data['tag']
            image = form.cleaned_data['image']
            u = Image()
            u.tag = tag
            u.title = title
            u.image = image
            u.save()
            return redirect('upload')
    else:
        form = ImageForm()
    return render(request, 'upload/model_form_upload.html', {'form': form} )