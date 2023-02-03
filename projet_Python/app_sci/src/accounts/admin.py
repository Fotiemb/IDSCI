from django.contrib import admin
from accounts.models import Data


class DataPostAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "telephone")


admin.site.register(Data, DataPostAdmin)
