from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import EmailValidator


class User(AbstractUser, PermissionsMixin):
    first_name = models.CharField("Имя", max_length=150, blank=True)
    last_name = models.CharField("Фамилия", max_length=150, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)

    email = models.EmailField("Почта", blank=True, validators=[EmailValidator], unique=True)
    email_verified = models.BooleanField(default=False)

    city = models.CharField(max_length=100, blank=True, null=True)

    birth_date = models.DateField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"