from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth import get_user_model
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


class UsersView(ListView):
    model = SiteUser
    paginate_by = 2
    template_name = "users/elements/users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = SiteUser.objects.all()
        print(context)
        return context


class UpdateUser(UpdateView):
    model = SiteUser
    form_class = CustomUserChangeForm
    success_url = 'users'
    template_name = "users/pages/users/user_edit.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = SiteUser.objects.get(pk=pk)
        return context


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/pages/users/login.html'

    def get_success_url(self):
        return reverse_lazy('welcome_page')


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/pages/users/user_create.html'

    def get_success_url(self):
        return reverse_lazy('welcome_page')
