from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password, nickname, is_superuser, is_staff):
        now = timezone.now()
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(
                 email=email,
                 nickname=nickname,
                 is_active=True,
                 is_superuser=is_superuser,
                 is_staff=is_staff,
                 last_login=now,
                 )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, nickname, **extra_fields):
        return self._create_user(email, password, nickname, False, False, **extra_fields)

    def create_superuser(self, email, password, nickname,  **extra_fields):
        user = self._create_user(email, password, nickname, True, True, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True, db_index=True, max_length=30)
    joined = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_image = models.ImageField(null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email', 'nickname']
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return ""

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
