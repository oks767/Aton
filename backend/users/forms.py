from django import forms
from users.models import User
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите фамилию'}))
    patronymic = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите отчество'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronymic', 'username', 'email', 'password1', 'password2')
