from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms

from users.models import SiteUser



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = SiteUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = SiteUser
        fields = ('first_name', 'last_name', 'username', 'language', 'gender', 'email', 'address', 'birthday', 'phone', 'city')
        widgets = {
            'language': forms.RadioSelect(),
            'gender': forms.RadioSelect(),
        }
