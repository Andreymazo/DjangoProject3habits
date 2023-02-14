from django import forms

from mailing.models import Client


#
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'