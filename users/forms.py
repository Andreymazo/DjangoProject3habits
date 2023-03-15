from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from base.forms import StyleFormMixin
from users.models import User

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