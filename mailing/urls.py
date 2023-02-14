from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView

# mailing,
app_name = MailingConfig.name

urlpatterns = [
    # path('', mailing, name='login'),
    path('', ClientListView.as_view(), name='login'),#'template_name=mailing/index1.html'
    path('client', ClientCreateView.as_view(), name='create')

]