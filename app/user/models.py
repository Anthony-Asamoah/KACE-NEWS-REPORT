from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.choices import ROLE_CHOICES


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='reporter')

    def __str__(self):
        return self.username
