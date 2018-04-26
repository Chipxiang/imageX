from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import auth
from django.urls import reverse ,reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .forms import LoginForm,InvitationForm
from .models import Member, Profile
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.translation import ugettext as _
from .forms import RegisterForm,UserEditForm, ProfileEditForm
from .token_generator import modified_token_generator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def profile(request,filename):
    member = get_object_or_404(Member, username=filename)
    return render(request, 'account/profile.html', {'member': member, 'section': 'images'})



def dashboard(request):
    member = Member.objects.get(username=request.user.username)
    return render(request, 'account/homepage.html', {'member':member, 'section': 'dashboard'})


def user_register(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            member = auth.authenticate(username=username, password=password)

            if member:
                context['userExit'] = True
                return HttpResponse("already exits")

            member = Member.objects.create_user(username=username, password=password, email=email)
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

            member = authenticate(username=username, password=password)

            if member:
                auth.login(request, member)
                request.session['username'] = username
                return HttpResponseRedirect(reverse("account:dashboard"))
            else:
                return HttpResponse("Invalid User or Password")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def user_logout(request):

    auth.logout(request)
    #return HttpResponseRedirect(reverse("search:searchImage"))
    return render(request, 'account/logout.html' )

def invite_newmemeber(request,
                   template_name='account/invite.html',
                   email_template_name='account/invite_email.html',
                   subject_template_name='account/invite.txt',
                   token_generator=modified_token_generator,
                   post_reset_redirect=reverse_lazy('account:invite_done'),
                   html_email_template_name=None):

    member = Member.objects.get(username=request.user.username)
    from_email = member.email

    if request.method == "POST":
        form = InvitationForm(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
            }


            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = InvitationForm()
    context = {
        'form': form,
        'title': _('Password reset'),
        'section': 'invite'
    }

    return TemplateResponse(request, template_name, context)


def invite_done(request,
                template_name='account/invite_done.html',):

    return TemplateResponse(request, template_name)

def invite_confirm(request, token=None,
                    template_name='account/invite_confirm.html',
                    token_generator=modified_token_generator,
                     ):

        email = None
        assert token is not None
        if request.session.has_key('email'):
              email = request.session['email']
        auth.logout(request)
        post_reset_redirect = reverse('search:search')
        form = None
        if token_generator.check_token(token):
            validlink = True
            title = _('Enter new Username')
            if request.method == 'POST':
                form = RegisterForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']

                    member = auth.authenticate(username=username, password=password)

                    if member:
                        return HttpResponse("already exits")
                    member = Member.objects.create_user(username=username,
                                                        password=password, email=email)
                    profile = Profile.objects.create(user=member)
                    member.save()
                    profile.save()
                    return HttpResponseRedirect(post_reset_redirect)

        else:
            validlink = False
            title = _('invitation unsuccessful')
        context = {
            'form': form,
            'title': title,
            'validlink': validlink,
        }
        return TemplateResponse(request, template_name, context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated ' \
                                      'successfully')
        else:
            messages.error(request, 'Error updating your profile')


    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})





PASSWORD_EMAIL_SENDER = 'noreply@hola-inc.top'

PASSWORD_RESET_TOKEN_REGEX = r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$'

PASSWORD_RESET_DONE_MSG = r"""

    We've emailed you instructions for setting your password, if an account exists with the email you entered.

    You should receive them shortly.



    If you don't receive an email, please make sure you've entered the address you registered with,"

    and check your spam folder.

"""


PASSWORD_RESET_EX_MSG = r"""

    The password reset link was invalid, possibly because it has already been used.

    Please request a new password reset.

"""


PASSWORD_RESET_COMPLETE = """

Your password has been set.

You may go ahead and login now.

"""