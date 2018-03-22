from django.shortcuts import render,redirect
from .forms import ImageForm

def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = ImageForm()
    return render(request, 'upload/model_form_upload.html', {'form': form} )