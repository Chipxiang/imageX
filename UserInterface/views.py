from django.shortcuts import render, redirect

def home(request, Username):

    return render(request, 'UserInterface/homepage.html', {'Username': Username })

def makeUpload(request, Username):
    return redirect('upload/')
