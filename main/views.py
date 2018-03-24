from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import UserForm
from .models import Member


def main(request):

    return render(request, 'main/home.html',)


def register_view(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user:
                context['userExit'] = True
                return render(request, 'main/reg.html', context)

            user = User.objects.create_user(username=username, password=password)
            user.save()

            member = Member(username=username)
            member.save()

            request.session['username'] = username

            auth.login(request, user)

            return redirect('/')
    else:
        context = {'isLogin': False}

    return render(request, 'main/reg.html', context)

def login_view(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username = username,password = password)
            if user:

                auth.login(request,user)
                request.session['username'] = username
                return redirect('/User='+username+'/' )
            else:

                context = {'isLogin': False,'pawd':False}
                return render(request, 'main/login.html', context)
    else:
        context = {'isLogin': False, 'pswd':True}
    return render(request, 'main/login.html', context)

def logout_view(request):

    auth.logout(request)
    return redirect('')
