from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.EmailField('email address', unique=True, db_index=True, max_length=30)
    joined = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
