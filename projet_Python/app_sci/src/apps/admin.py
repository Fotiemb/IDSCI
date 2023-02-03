from django.contrib import admin

from apps.models import BookModel


class BookAdmin(admin.ModelAdmin):
    list_display = ("auteur", "libelle", "exemplaire", "domaine", "photo")


admin.site.register(BookModel, BookAdmin)
