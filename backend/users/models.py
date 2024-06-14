from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Модель ответственного лица """
    patronymic = models.CharField(max_length=50, verbose_name="отчество")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
