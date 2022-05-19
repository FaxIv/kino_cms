from django.contrib.auth.models import AbstractUser
from django.db import models


class NewUser(AbstractUser):
    about = models.CharField(max_length=100)

