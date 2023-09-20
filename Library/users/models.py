from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    avatar = models.ImageField(default='users/profile-icon.jpg')

    def __str__(self):
        return self.username





