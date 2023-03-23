from django.contrib.auth.views import LoginView
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from rest_framework import generics, permissions
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from mailing.forms import SigninForm, SignupForm

from users.forms import UserRegisterForm, HabitForm, UserForm
from users.models import User, Habit
from users.seriaizers import HabitSerializer


class UserLoginView(LoginView):
    model = User
    # form_class = UserCustomCreationForm
    success_url = reverse_lazy('users:habit_list')
    template_name = 'users/login.html'


class SignupView(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('users:habit_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
        return super().form_valid(form)


# class CustomRegisterView(CreateView):
#     model = User
#     form_class = UserRegisterForm
#
#     def form_valid(self, form):
#         if form.is_valid():
#             self.object = form.save()
#
#             # if form.data.get('need_generate', False):
#             #     self.object.set_password(
#             #         self.object.make_random_password(length=12)
#             #     )
#             #     self.object.save()
#             self.object.is_active = False
#             # send_register_mail()
#             self.object.save()
#         return super().form_valid(form)

class Habit_listAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_active:
            return queryset.filter(client=self.request.user) ## Kazhdii mozhet smotret tolko svoi privichki
        return queryset

class Habit_createAPIView(generics.CreateAPIView, CreateModelMixin):#, HabitForm
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_active:
            return queryset.filter(client=self.request.user)  ## Kazhdii mozhet sozdavat tolko svoi privichki
        return queryset
    # def get_queryset(self):
    #     if self.request.method == 'GET':
    #         return models.Book.objects.all()
    #     else:
    #         return models.Book.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

class IsAuthorOrIsAuthenticated(permissions.BasePermission): #(Voobshe ushlo pole client, to est sozdaut svoi tolko)

        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return bool(request.user and request.user.is_authenticated)
            return obj.client == request.user

    # HabitForm.save(self=)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # def smth(self, request):
    #     if request.method == 'POST':
    #         if HabitForm.is_valid():
    #             try:
    #                 HabitForm.save()
    #                 return Response(serializer.data, status=status.HTTP_201_CREATED)
    #             except:
    #                 pass
    #     else:
    #         raise ValidationError



#     permission_classes = (RulesCreateLesson,)
class Habit_updateAPIView(generics.UpdateAPIView, UpdateModelMixin):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

class Habit_deleteAPIView(generics.DestroyAPIView, DestroyModelMixin):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

def change_status(request, pk):##Kogda detail ili delete budem ispolzovat
    if request.user.has_perm('catalog.set_is_published'):

    # product_item = Product.objects.filter(pk=pk).first()
    # if product_item:
    #     if ... is None:
        habit_item = get_object_or_404(Habit, pk=pk)
        if habit_item.is_published:
            habit_item.published_status = True
        else:
            habit_item.published_status = True
        habit_item.save()
        return redirect(reverse('users:habit_list'))

    raise HttpResponseBadRequest
class UserListView(ListView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('mailing:Client_update')
    template_name = 'mailing/Client1.html'
    # def get_queryset(self):#Pochemu to ne filtruet po useru, a vse ubiraet, poka zakommentim
    #     print('--------------------', self.request.user)##email polzovatelia
    #
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_active:
            return queryset.filter(is_staff=True) ## Kazhdii mozhet smotret tolko svoi rassilki
        return queryset

class UserView(CreateView):#Posle registracii/logina Client popadaet v etu formu, a ne na Client_list (emu znat vseh clientov ne nado
    #################Potom ClientListView zakommentiruu
    model = User
    form_class = UserForm
    success_url = 'mailing:Client_withsubject'##Posle sozdania perenapravliaem na obshuu stranicu
    template_name = 'mailing/Client_create.html'##Ishem modul bootstrap

    def form_valid(self, form):##Chtobi chuzhoe ne trogali
        if form.is_valid():
            form.save(commit=False)
            self.object.email = self.request.user##Dobaliaem pole - znachenie polzovatelia/ mozhet ne email, a name
            self.object.save()
        return super(UserView, self).form_valid()
# class HabitUpdateViewWithSubject(CreateView):
#     model = Habit
#     form_class = HabitForm
#     success_url = reverse_lazy('mailing:Client_list')
#     template_name = 'mailing/user_withsubject.html'
# #
# #     # def clean_product_content(self):
# #     #     t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
# #     #     if self.request.method == 'POST':
# #     #         # form = ProductForm(request.POST, request.FILES)
# #     #         for i in t:
# #     #             if self.product_content == i:
# #     #                 raise ValueError('Nedopustimie slova')
# #     # def get_success_url(self):
# #     #     return reverse('catalog:Product_list', args=[self.object.pk])
# #
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         FormSet = inlineformset_factory(self.model, Subject, form=SubjectForm, extra=1)
#
#         if self.request.method == 'POST':
#             formset = FormSet(self.request.POST, instance=self.object)
#         else:
#             formset = FormSet(instance=self.object)
#
#         context_data['formset'] = formset
#         return context_data
#
#     def form_valid(self, form):
#         f = Subject.objects.all().filter(name_id=self.request.user.id) ##Otsilaem po emeilam otnosyashimsya k activnomu polzovatelu
#         context_data = self.get_context_data()
#         formset = context_data['formset']
#         # print(self.request.method)
#         with transaction.atomic():
#             self.object = form.save()
#             if formset.is_valid():
#                 formset.instance = self.object
#                 formset.save()
#                 # print(self.object.link)
#                 for i in f:
#                     print(i.email)
#                     print('form.instance ', form.instance, 'i.period ------------', i.period) ##ne menyaetsya period v subjecte
#                     # time.sleep(Subject.period(self.request.user))
#                     # send(i.email)
#                 # send(form.instance.link)
#
#             else:
#                 return super(UserUpdateViewWithSubject, self).form_invalid(form)
#         return super(UserUpdateViewWithSubject, self).form_valid(form)

class UserUpdateViewWithHabit(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('mailing:Client_list')
    template_name = 'mailing/user_withsubject.html'

    def form_valid(self, form):  ##Chtobi chuzhoe ne trogali
        if form.is_valid():
            form.save(commit=False)
            self.object.email = self.request.user  ##Dobaliaem pole - znachenie polzovatelia/ mozhet ne email, a name
            self.object.save()
        return super(UserUpdateViewWithHabit, self).form_valid()
#     # def clean_product_content(self):
#     #     t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
#     #     if self.request.method == 'POST':
#     #         # form = ProductForm(request.POST, request.FILES)
#     #         for i in t:
#     #             if self.product_content == i:
#     #                 raise ValueError('Nedopustimie slova')
#     # def get_success_url(self):
#     #     return reverse('catalog:Product_list', args=[self.object.pk])
#
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(self.model, Habit, form=HabitForm, extra=1)

        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        #f = Habit.objects.all().filter(name_id=self.request.user.id) ##Otsilaem po emeilam otnosyashimsya k activnomu polzovatelu
        context_data = self.get_context_data()
        formset = context_data['formset']
        # print(self.request.method)
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
                # print(self.object.link)
                # for i in f:
                #     print(i.email)
                #     print('form.instance ', form.instance, 'i.period ------------', i.period) ##ne menyaetsya period v subjecte
                    # time.sleep(Subject.period(self.request.user))
                    # send(i.email)
                # send(form.instance.link)

            else:
                return super(UserUpdateViewWithHabit, self).form_invalid(form)
        return super(UserUpdateViewWithHabit, self).form_valid(form)
