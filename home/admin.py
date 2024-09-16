from django.contrib import admin
from . import models


@admin.register(models.ContactUsMessage)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email')
