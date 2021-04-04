from django.contrib import admin

from .models import Contact, Client


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'messages')


admin.site.register(Contact)
admin.site.register(Client)
