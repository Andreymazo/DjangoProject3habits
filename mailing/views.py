import time
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.core.management import BaseCommand
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, CreateView, ListView, UpdateView, TemplateView

from mailing.forms import ClientForm, SignupForm, SigninForm



# class SigninView(LoginView):
#     template_name = 'mailing/login.html'
#     form_class = SigninForm


# class SignupView(CreateView):
#     template_name = 'mailing/register.html'
#     model = Client
#     form_class = SignupForm
#     success_url = reverse_lazy('mailing:Client_list')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         self.object = form.save()
    #         set_verify_token_and_send_mail(self.object)
    #     return super().form_valid(form)
# class VerifySuccessView(TemplateView):
#     success_url = reverse_lazy('mailing:Client_list')
#     template_name = 'mailing/register.html'

# class ClientListView(ListView):
#     model = Client
#     form_class = ClientForm
#     success_url = reverse_lazy('mailing:Mssg_list')
#     template_name = 'mailing/Client_list.html'



# class ClientCreateView(CreateView):#Zapretili sozdanie producta
#     model = Client
#     # permission_required = 'catalog.create_Product'
#     #form_class = SubjectForm
#     form_class = ClientForm
#     # fields = ('product_name', 'product_description', 'preview', 'price_per_unit', 'category')
#     success_url = reverse_lazy('mailing:Client_list')
#     template_name = 'mailing/Client_list.html'
#
#
# class ClientUpdateView(UpdateView):#LoginRequiredMixin,
#     model = Client
#     # form_class = ClientForm
#     # success_url = reverse_lazy('catalog:Product_list')
#     template_name = 'mailing/Client_list.html'

#
# class ClientDeleteView(DeleteView):#UserPassesTestMixin,
#     model = Client
#     form_class = ClientForm
#     success_url = reverse_lazy('catalog:Product_list')
#     template_name = 'catalog/product_confirm_delete.html'
#
#     # def test_func(self):
#     #     return self.request.user.is_superuser
#
#
# class ClientDetailView(DetailView):#LoginRequiredMixin,
#     model = Client
#     # form_class = ProductForm
#     success_url = reverse_lazy('catalog:Product_list')
#     template_name = 'catalog/Product_detail.html'
#######################Primer sozdania formi dlia zapolnenia polya
# from django import forms
# from django.shortcuts import get_object_or_404
#
# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ("name", )
#
# def bound_form(request, id):
#     item = get_object_or_404(Item, id=id)
#     form = ItemForm(instance=item)
#     return render_to_response('bounded_form.html', {'form': form})