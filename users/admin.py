from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import SiteUser, MailFiles


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = SiteUser


admin.site.register(SiteUser, CustomUserAdmin)
admin.site.register(MailFiles)
