from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteUser(AbstractUser):
    LANGUAGE = (
        ('uk', _('Українська')),
        ('ru', _('Російська')),
    )

    GENDER = (
        ('male', _('Чоловіча')),
        ('female', _('Жіноча')),
    )

    CITY = (
        ('Київ', _('Київ')),
        ('Харків', _('Харків')),
        ('Одеса', _('Одеса')),
        ('Львів', _('Львів')),
        ('Дніпро', _('Дніпро')),
    )

    language = models.CharField(max_length=30, choices=LANGUAGE, default='uk')
    gender = models.CharField(max_length=30, choices=GENDER)
    phone = models.PositiveIntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=150, choices=CITY, null=True, blank=True)

    objects = BaseUserManager()

    def __str__(self):
        return self.username
