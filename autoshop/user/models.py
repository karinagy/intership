from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(('username'), max_length=255, unique=True)
    email = models.EmailField(('email address'),
                              null=True, blank=True)
    phone = models.CharField(('phone number'), max_length=30,
                             null=True, blank=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=False)
    is_staff = models.BooleanField(('staff'), default=False)

    is_verified = models.BooleanField(('verified'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ['username', 'email', 'phone']
