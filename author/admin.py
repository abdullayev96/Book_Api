from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'bio', 'photo','book_number')

    list_filter = ('full_name', 'bio')
    search_fields = ("full_name",)


admin.site.register(Author, AuthorAdmin)
