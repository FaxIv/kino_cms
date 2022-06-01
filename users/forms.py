from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from users.models import SiteUser



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = SiteUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = SiteUser
        fields = '__all__'
        # fields = ('username',)
