from django.shortcuts import render,redirect
from .forms import ImageForm
from main.models import Image , Member

def upload(request, Username):

    member = Member.objects.get(username=Username)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            description = form.cleaned_data['description']
            tag = form.cleaned_data['tag']
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
            return redirect('/main/')
    else:
        form = ImageForm()
    return render(request, 'upload/model_form_upload.html', {'form': form ,'username': Username} )