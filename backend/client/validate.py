from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_birth_date(value):
    birth_date = timezone.now().date()
    if value > birth_date:
        raise ValidationError(f"Неверно указана дата рождения! {birth_date} еще не наступило ")

    age = timezone.now().year - value.year - ((timezone.now().month, timezone.now().day) < (value.month, value.day))
    if age > 130:
        raise ValidationError("Возраст не может превышать 130 лет")


def validate_account_number(number):
    if not number.isdigit():
        raise ValidationError("Номер счета должен состоять только из цифр")

    if 20 > len(number) < 20:
        raise ValidationError("Номер счета должен состоять из 20 цифр")


def validate_inn(inn):
    if not inn.isdigit():
        raise ValidationError("Номер ИНН должен состоять только из цифр")

    if 10 > len(inn) < 10:
        raise ValidationError("Номер ИНН должен состоять из 10 цифр")
