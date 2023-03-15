from django.contrib.auth.views import LoginView
from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from mailing.forms import SigninForm, SignupForm
from users.forms import UserRegisterForm
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

class Habit_createAPIView(generics.CreateAPIView, CreateModelMixin):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

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

