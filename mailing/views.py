import time

from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, CreateView, ListView, UpdateView

from mailing.forms import ClientForm
from mailing.models import Client, Mssg


class Command(BaseCommand):

    def handle(self, *args, **options):
# def mailing(request):#
        m=Client.objects.select_related("topic", "comment").all()
        print(m)
#         emails1 = ['andreymazo@mail.ru', 'andreymazo2@mail.ru']
#         emails2 = ['andreymazo@mail.ru', 'andreymazo2@mail.ru']
#         emails=[emails1, emails2]
#         while Mssg.status:
#             for i in emails:
#                 time.sleep(m.Mssg.period)
#                 if request.method == 'GET':
#                 # res = "Zaglushka chtobi ne otpravlyat pisma"
#                 res = send_mail(
#                     subject=' test subject ',
#                     message=f' test message ',
#                     from_email=settings.EMAIL_HOST_USER,
#                     recipient_list=i,
#                     fail_silently=False,
#                     auth_user=None,
#                     auth_password=None,
#                     connection=None,
#                     html_message=None,
#                 )
#                   if res:
#                       Attempt.objects.create(
#                           status = res,
#                           response=''
#                       )
#                 Mailinglog.objects.create(
#                     message=item.message,
#                     mailing=item,
#                     result=res
#                 )
# #
#                 # context = {'object_list': Mssg.objects.all()}
#                 print(f'Messg sent >>>>>>, Result, {res}')#{Client.comment_set.count}
#                 context = {'res':res}
#                 return render(request, 'mailing/index1.html', context)
#
# from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
# Here’s an example view that takes a subject, message and from_email from the request’s POST data, sends that to admin@example.com and redirects to “/contact/thanks/” when it’s done
# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['admin@example.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')



class ClientListView(ListView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:login')
    template_name = 'mailing/index1.html'



class ClientCreateView(CreateView):#Zapretili sozdanie producta
    model = Client
    # permission_required = 'catalog.create_Product'
    #form_class = SubjectForm
    form_class = ClientForm
    # fields = ('product_name', 'product_description', 'preview', 'price_per_unit', 'category')
    # success_url = reverse_lazy('catalog:Product_list')
    template_name = 'mailing/index1.html'


class ClientUpdateView(UpdateView):#LoginRequiredMixin,
    model = Client
    # form_class = ClientForm
    # success_url = reverse_lazy('catalog:Product_list')
    template_name = 'mailing/index1.html'

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