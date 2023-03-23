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

        # class HabitForm(ModelForm):
        #     model = Habit
        #     fields = '__all__'
    def clean(self):
        clean_data = super(HabitForm, self).clean()  # HabitForm, self
        if_connected = clean_data['if_connected']
        prize = clean_data['prize']
        if if_connected and prize:
            raise ValidationError("You may not choose both fields!")

        return clean_data
    # def clean_if_connected(self):
    #     if_connected=self.clean_if_connected['if_connected']
    #     prize = self.clean_if_connected['prize']
    #     if if_connected and prize:
    #         raise ValidationError
    #     return if_connected
    # def clean_prize(self):
    #     if_connected = self.clean_prize['if_connected']
    #     prize = self.clean_prize['prize']
    #     if if_connected and prize:
    #         raise ValidationError
    #     return prize

