from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password, nickname, is_admin, is_superuser):
        now = timezone.now()
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(
                 email=email,
                 nickname=nickname,
                 is_admin=is_admin,
                 is_active=False,
                 is_superuser=is_superuser,
                 last_login=now,
                 )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, nickname, **extra_fields):
        return self._create_user(email, password, nickname, False, False, **extra_fields)

    def create_superuser(self, email, password, nickname,  **extra_fields):
        user = self._create_user(email, password, nickname, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField('email address', unique=True, db_index=True, max_length=30)
    joined = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email', 'nickname']
    objects = UserManager()

    def __str__(self):
        return self.email
