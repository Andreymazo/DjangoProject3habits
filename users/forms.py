from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from base.forms import StyleFormMixin

from users.models import User, Habit


class UserSigninForm(StyleFormMixin, AuthenticationForm):
    pass


class UserSignupForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
        # field_classes = {"username": UsernameField}


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = '__all__'#['action', 'if_connected', 'prize', 'place', 'period']



