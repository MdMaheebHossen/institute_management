from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    USER_TYPE = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    ]
    user_type = models.CharField(choices=USER_TYPE, max_length=20, null=True)

    def __str__(self):
        return f'{self.username}'