from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from . import views
app_name = "account"
urlpatterns = [

    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'register/$', views.user_register,name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^invite/$', views.invite_newmemeber, name='invite'),
    url(r'^invite/done$', views.invite_done, name='invite_done'),

    url(r'^invite/confirm/(?P<token>[-\w]+)/$', views.invite_confirm, name='invite_confirm'),

    url(r'^password-change/$', password_change,
       name='password_change'),

    url(r'^password-change/done/$', password_change_done,
        name='password_change_done'),

    url(r'^password-reset/$', lambda request, **kwargs: password_reset(
        request, template_name='registration/password_reset.html',
        email_template_name='registration/password_reset_email.html',
        post_reset_redirect=reverse_lazy('account:password_reset_done'),
        extra_context={
            'validlink': True,
        },  **kwargs

        ), name='password_reset'),


    url(r'^password-reset-done/$', lambda request, **kwargs: password_reset_done(
        request,
        template_name='registration/password_reset_done.html',

        ), name='password_reset_done'),

    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
            lambda request, **kwargs: password_reset_confirm(

              request, template_name='registration/password_reset_confirm.html',
              post_reset_redirect=reverse_lazy('account:password_reset_complete'),
              extra_context={
                    'form_title': 'Reset Password',
                    'form_submit': 'Reset',
                    'exception_msg': views.PASSWORD_RESET_EX_MSG,
                }, **kwargs

            ), name='password_reset_confirm'),

    url(r'^password-reset-complete/$', lambda request, **kwargs: password_reset_complete(

          request, template_name='registration/password_reset_complete.html',
      ), name='password_reset_complete'),

]


