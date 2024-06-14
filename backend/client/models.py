from django.db import models
from users.models import User
from client.validate import validate_birth_date, validate_account_number, validate_inn


class Client(models.Model):
    """ Таблица клиентов """

    STATUS_CHOICES = (
        ("В работе", "В работе"),
        ("Отказ", "Отказ"),
        ("Сделка закрыта", "Сделка закрыта"),
        ("Не в работе", "Не в работе")
    )
    account_number = models.CharField(
        max_length=20,
        unique=True,
        validators=[validate_account_number],
        verbose_name="номер счета"
    )
    surname = models.CharField(max_length=50, verbose_name="фамилия")
    name = models.CharField(max_length=50, verbose_name="имя")
    patronymic = models.CharField(max_length=50, verbose_name="отчество")
    date_birth = models.DateField(verbose_name="дата рождения", validators=[validate_birth_date])
    inn = models.CharField(
        max_length=12,
        unique=True,
        verbose_name="инн",
        validators=[validate_inn]
    )
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ответственный")
    status = models.CharField(
        max_length=14,
        choices=STATUS_CHOICES,
        default="Не в работе",
        verbose_name="статус"
    )

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"

    def update_status(self, new_status):
        self.status = new_status
        self.save()
