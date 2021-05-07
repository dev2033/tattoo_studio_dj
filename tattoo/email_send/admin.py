from django.contrib import admin

from .models import Contact, Client


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Client, ClientAdmin)
