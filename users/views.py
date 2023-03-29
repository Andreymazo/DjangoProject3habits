import datetime
import time

import pytz
import requests
import telepot
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from rest_framework import generics, permissions
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from config import settings
from mailing.forms import SigninForm, SignupForm

from users.forms import UserRegisterForm, HabitForm, UserForm
from users.models import User, Habit
from users.seriaizers import HabitSerializer
from users.tasks import send_telegram


#from users.tasks import send_message


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
            return queryset.filter(client=self.request.user)  ## Kazhdii mozhet smotret tolko svoi privichki
        return queryset

    #Channel https: // t.me / habitst
    # BOT_CHAT_ID = settings.MY_CHAT_ID
    # telegramBot = telepot.Bot(settings.MY_CHAT_ID)
    # bot = telepot.Bot(settings.BOT_TOKEN)
    # #https://api.telegram.org/bot<token>/sendMessage?chat_id=<chatId>&text=Hello
    # response = requests.get(f'https://api.telegram.org/bot{settings.BOT_TOKEN}/getupdates')
    # a = response.json()
    #{'ok': True, 'result': [{'update_id': 166459803, 'my_chat_member': {'chat': {'id': -1001902473862, 'title': 'HabitStudyMazo', 'username': 'habitst', 'type': 'channel'}, 'from': {'id': 5015736552, 'is_bot': False, 'first_name': 'Andrey', 'last_name': 'Mazo', 'username': 'AndreyMazo'}, 'date': 1680003349, 'old_chat_member': {'user': {'id': 6193506005, 'is_bot': True, 'first_name': 'habit_reminder', 'username': 'habit_reminderbot'}, 'status': 'left'}, 'new_chat_member': {'user': {'id': 6193506005, 'is_bot': True, 'first_name': 'habit_reminder', 'username': 'habit_reminderbot'}, 'status': 'administrator', 'can_be_edited': False, 'can_manage_chat': True, 'can_change_info': False, 'can_post_messages': False, 'can_edit_messages': False, 'can_delete_messages': False, 'can_invite_users': False, 'can_restrict_members': True, 'can_promote_members': False, 'can_manage_video_chats': False, 'is_anonymous': False, 'can_manage_voice_chats': False}}}, {'update_id': 166459804, 'my_chat_member': {'chat': {'id': -1001902473862, 'title': 'HabitStudyMazo', 'username': 'habitst', 'type': 'channel'}, 'from': {'id': 5015736552, 'is_bot': False, 'first_name': 'Andrey', 'last_name': 'Mazo', 'username': 'AndreyMazo'}, 'date': 1680003643, 'old_chat_member': {'user': {'id': 6193506005, 'is_bot': True, 'first_name': 'habit_reminder', 'username': 'habit_reminderbot'}, 'status': 'administrator', 'can_be_edited': False, 'can_manage_chat': True, 'can_change_info': False, 'can_post_messages': False, 'can_edit_messages': False, 'can_delete_messages': False, 'can_invite_users': False, 'can_restrict_members': True, 'can_promote_members': False, 'can_manage_video_chats': False, 'is_anonymous': False, 'can_manage_voice_chats': False}, 'new_chat_member': {'user': {'id': 6193506005, 'is_bot': True, 'first_name': 'habit_reminder', 'username': 'habit_reminderbot'}, 'status': 'administrator', 'can_be_edited': False, 'can_manage_chat': True, 'can_change_info': False, 'can_post_messages': True, 'can_edit_messages': False, 'can_delete_messages': False, 'can_invite_users': False, 'can_restrict_members': True, 'can_promote_members': False, 'can_manage_video_chats': False, 'is_anonymous': False, 'can_manage_voice_chats': False}}}, {'update_id': 166459805, 'my_chat_member': {'chat': {'id': -1001902473862, 'title': 'HabitStudyMazo', 'username': 'habitst', 'type': 'channel'}, 'from': {'id': 5015736552, 'is_bot': False, 'first_name': 'Andrey', 'last_name': 'Mazo', 'username': 'AndreyMazo'}, 'date': 1680003668, 'old_chat_member': {'user': {'id': 6193506005, 'is_bot': True, 'first_name': 'habit_reminder', 'username': 'habit_reminderbot'}, 'status': 'administrator', 'can_be_edited': False, 'can_manage_chat': True, 'can_change_info': False, 'can_post_messages': True, 'can_edit_messages': False, 'can_delete_messages': False, 'can_invite_users': False, 'can_restrict_members': True, 'can_promote_members': False, 'can_manage_video_chats': False, 'is_anonymous': False, 'can_manage_voice_chats': False}, 'new_chat_member': {'user': {'id': 6193506005, 'is_bot': True, 'first_name': 'habit_reminder', 'username': 'habit_reminderbot'}, 'status': 'administrator', 'can_be_edited': False, 'can_manage_chat': True, 'can_change_info': True, 'can_post_messages': True, 'can_edit_messages': True, 'can_delete_messages': True, 'can_invite_users': True, 'can_restrict_members': True, 'can_promote_members': False, 'can_manage_video_chats': True, 'is_anonymous': False, 'can_manage_voice_chats': True}}}, {'update_id': 166459806, 'channel_post': {'message_id': 2, 'sender_chat': {'id': -1001902473862, 'title': 'HabitStudyMazo', 'username': 'habitst', 'type': 'channel'}, 'chat': {'id': -1001902473862, 'title': 'HabitStudyMazo', 'username': 'habitst', 'type': 'channel'}, 'date': 1680003871, 'text': 'test'}}]}
#System check identified no issues (0 silenced).

    # requests.get(f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={settings.BOT_CHAT_ID}&text=Hello World!')
    ############################################################Otsilaet v channel 'Hello world'

    def get(self, request, *args,
           **kwargs):  ##Funcia v sluchae esli pole time_to_doo_habit > 30 sec time, chego to delaet
        if request.method == 'GET':
            send_telegram(self, request)#zapuskaet task (tam otsilka zacommenchana

        textt = 'Time waits for nobody'
        while True:
            if request.method == 'GET':
                text = 'something'
                time.sleep(35)  ##Kazhdie 30 sec proveryaet pole time_to_doo_habit

                # thread = threading.Thread(  # создание отдельного потока
                #     target=print, args=("данные сайта обновились",))
                # thread.start()
                #now = time.time()
                now = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
                a = Habit.objects.all()  # time_to_doo_habit.second
                for ii in User.objects.all():
                    for i in Habit.objects.all().filter(client_id=ii):
                        time_compare = (now - i.updated_at).total_seconds() % 86400
                        #seconds = ((i.time_to_doo_habit.hour * 60 + i.time_to_doo_habit.minute) * 60 + i.time_to_doo_habit.second)
                        try:
                            seconds = ((
                                                   i.time_to_doo_habit.hour * 60 + i.time_to_doo_habit.minute) * 60 + i.time_to_doo_habit.second)
                            if abs(time_compare-seconds) > 30:  # Esli menshe polminuti do vremeni, otsilaem
                                print('Otsilaem*****************')  ###Zdes mozhno otsilat v telegramm
                                response = requests.post(
                                    f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={settings.CHAT_ID}&text={i.action}')
                                print(
                                    response.json())  # {'ok': False, 'error_code': 400, 'description': 'Bad Request: chat not found'}
    #                             send_message(text)
    #                             if seconds:
    #                                 response = requests.post(
    #                                     f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={settings.CHAT_ID}&text={i.action}')#Proverka
    #                                 print(
    #                                     response.json())
                        except AttributeError as e:
                            print(e)
                            pass
                        except TypeError as e:
                            print(e)
                            pass
    #                 # for i in a:
    #                 #     print(dir(i))
    #                 # delta = abs(Habit.time_to_doo_habit.second - now)
    #                 print('now++++++++++++++++++++++', now)
    #                 # if delta < 30:
    #                 #     # if self.pk is not None:
    #                 #     #     now = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
    #                 #     print('delta', delta)
    #                 response = requests.post(
    #                     f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={settings.CHAT_ID}&text=Hello World!')
    #                 print(response.json())#{'ok': False, 'error_code': 400, 'description': 'Bad Request: chat not found'}
    #
    #                 # response = requests.post(
    #                 #     url=f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage',
    #                 #     data={'chat_id': " -1001902473862", 'text': 'hello friend'}#settings.MY_CHAT_ID
    #                 # )
    #
    #                 print(response.json())
    #                 # bot = telepot.Bot(settings.BOT_TOKEN)
    #                 # bot.sendMessage(settings.CHAT_ID, textt)
    #                 print('++++++++++++++++++++++++')
            return self.list(request, *args, **kwargs)
   ##################################################################################
    # def my_view(self, request):
    #         # <view logic>
    #         while True:
    #             if request.method == 'GET':
    #                 time.sleep(1)  ##Kazhdie 25v sec proveryaet pole time_to_doo_habit
    #                 # thread = threading.Thread(  # создание отдельного потока
    #                 #     target=print, args=("данные сайта обновились",))
    #                 # thread.start()
    #                 now = time.time()
    #                 delta = abs(Habit.time_to_doo_habit.second - now)
    #                 print('now-----------', now)
    #                 if delta < 30:
    #                     # if self.pk is not None:
    #                     #     now = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
    #                     print('delta', delta)
    #                 print('_______________________')
    #             return HttpResponse('result')
    # def get(self, request, *args, **kwargs):##Proveryaem na izmenenie polya
    #
    #     while True:
    #         if self.request
    #         time.sleep(5)##Kazhdie 25v sec proveryaet pole time_to_doo_habit
    #         # thread = threading.Thread(  # создание отдельного потока
    #         #     target=print, args=("данные сайта обновились",))
    #         # thread.start()
    #         now = time.time()
    #         delta = abs(self.time_to_doo_habit.second - now)
    #         print('now-----------',now)
    #         if delta < 30:
    #         # if self.pk is not None:
    #         #     now = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
    #             print('delta', delta)
    #         print('_______________________')
    #             # if (now - self.updated_at).seconds > 4*60*60:
    #             #     send_notify_update.delay(self/pk)
    #         super().


class Habit_createAPIView(generics.CreateAPIView, CreateModelMixin):  # , HabitForm
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


class IsAuthorOrIsAuthenticated(permissions.BasePermission):  # (Voobshe ushlo pole client, to est sozdaut svoi tolko)

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


def change_status(request, pk):  ##Kogda detail ili delete budem ispolzovat
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
            return queryset.filter(is_staff=True)  ## Kazhdii mozhet smotret tolko svoi rassilki
        return queryset


class UserView(
    CreateView):  # Posle registracii/logina Client popadaet v etu formu, a ne na Client_list (emu znat vseh clientov ne nado
    #################Potom ClientListView zakommentiruu
    model = User
    form_class = UserForm
    success_url = 'mailing:Client_withsubject'  ##Posle sozdania perenapravliaem na obshuu stranicu
    template_name = 'mailing/Client_create.html'  ##Ishem modul bootstrap

    def form_valid(self, form):  ##Chtobi chuzhoe ne trogali
        if form.is_valid():
            form.save(commit=False)
            self.object.email = self.request.user  ##Dobaliaem pole - znachenie polzovatelia/ mozhet ne email, a name
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
        # f = Habit.objects.all().filter(name_id=self.request.user.id) ##Otsilaem po emeilam otnosyashimsya k activnomu polzovatelu
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
