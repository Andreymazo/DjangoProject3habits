from django.contrib import admin

from mailing.models import Client, Mssg, Emails

# admin.site.register(Client)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(Mssg)

admin.site.register(Emails)

