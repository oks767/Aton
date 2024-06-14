from django.contrib import admin
from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'account_number',
        'surname',
        'name',
        'patronymic',
        'date_birth',
        'inn',
        'responsible',
        'status',
    )
