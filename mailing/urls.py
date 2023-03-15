from django.contrib.auth.views import LogoutView
from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import SigninView, SignupView, ClientListView, VerifySuccessView  # , ClientCreateView,

# mailing,
app_name = MailingConfig.name

urlpatterns = [
    # path('', mailing, name='login'),

    # path('', SigninView.as_view(template_name='mailing/login.html'), name='login'),#'template_name=mailing/Client1.html'
    # path('client_register', SignupView.as_view(), name='register'),
    path('login_success', SignupView.as_view(template_name='mailing/login.html'), name='login_success'),
    path('register_success', VerifySuccessView.as_view(template_name='mailing/Client_list.html'), name='register_success'),

    # path('client_logout', LogoutView.as_view(), name='logout'),



    # path('client_register', ClientListView.as_view(), name='register'),
    path('Client_list/', ClientListView.as_view(template_name='mailing/Client_list.html'), name='Client_list')

# Client_list/<int:pk>
]
# urlpatterns = [path('', SigninView.as_view(template_name='spa/login.html'), name='login'),
#                path('register', SignupView.as_view(template_name='spa/register.html'), name='register'),
#                path('home/', SignupView.as_view(template_name='spa/home.html'), name='home')
