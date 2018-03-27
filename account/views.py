from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .forms import LoginForm
from .models import Member


def dashboard(request):
    member = Member.objects.get(username=request.user.username)
    return render(request, 'account/homepage.html', {'member':member})


def user_register(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            member = auth.authenticate(username=username, password=password)
            if member:
                context['userExit'] = True
                return HttpResponse("already exits")

            member = Member.objects.create_user(username=username, password=password)
            member.save()



            request.session['username'] = username

            auth.login(request, member)

            return redirect('/')
    else:
        context = {'isLogin': False}

    return render(request, 'registration/reg.html', context)

def user_login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            member = authenticate(username = username, password = password)
            if member:

                auth.login(request, member)
                request.session['username'] = username
                return HttpResponseRedirect(reverse("account:dashboard"))
            else:

                return HttpResponse("not exist")
    else:
        context = {'isLogin': False, 'pswd':True}
    return render(request, 'account/login.html', context)

def user_logout(request):

    auth.logout(request)
    #return HttpResponseRedirect(reverse("search:searchImage"))
    return render(request, 'account/logout.html' )
