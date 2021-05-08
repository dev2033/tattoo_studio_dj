from django.contrib import admin

from .models import Contact, Client, Record


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')


class RecordAdmin(admin.ModelAdmin):
    list_display = ('client', 'email', 'first_name', 'last_name', 'phone', 'message')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Record, RecordAdmin)
