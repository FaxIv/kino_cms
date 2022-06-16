from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.views.generic.edit import ProcessFormView

from adminapp.views import base
from .forms import *
from .models import *

User = get_user_model()


def users(request):
    all_users = SiteUser.objects.all()
    context = {
        'all_users': all_users,
    }
    return render(request, "users/elements/users.html", context)


def user_edit(request, pk):
    site_user = SiteUser.objects.get(pk=pk)

    if not request.user.is_superuser:
        if site_user.is_superuser:
            return redirect('welcome_page')

    site_user_form = CustomUserChangeForm(request.POST or None, instance=site_user)
    if request.method == 'POST':
        if site_user_form.is_valid():
            print()
            print(f"pass --- {request.POST['password-field']}")
            if request.POST['password-field'] != '':
                site_user.set_password(request.POST['password-field'])
            site_user_form.save()
            messages.success(request, _(f"Користувача {site_user_form.instance.username} успішно збережено."))
            return redirect("/users")
        else:
            print(f"User form error ---> {site_user_form.errors}")
            messages.error(request, _("Дані хибні"))

    context = {
        'user_form': site_user_form,
    }
    return render(request, "users/pages/users/user_edit.html", context)


class UsersView(ListView):
    model = SiteUser
    template_name = "users/elements/users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = SiteUser.objects.all()
        return context


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/pages/users/login.html'

    def get_success_url(self):
        return reverse_lazy('welcome_page')


class LogoutStaffUser(LogoutView):
    next_page = 'login'


class LogoutUser(LogoutView):
    next_page = 'main_page'


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/pages/users/user_create.html'

    def get_success_url(self):
        return reverse_lazy('welcome_page')


def mailing_view(request):
    site_users = SiteUser.objects.all()
    email_files = MailFiles.objects.all()

    # if request.method == 'POST':
    #
    # else:
    context = {
        'site_users': site_users,
        'email_files': email_files,
    }
    return render(request, 'users/elements/mailing.html', context)


class MailingUsersView(ListView):
    paginate_by = 10
    model = SiteUser
    template_name = 'users/pages/mailing/user_mailing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = SiteUser.objects.all()
        return context
