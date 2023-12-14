from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin



class FileBookInline(admin.StackedInline):
    model = FileBook




class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'author','performer', 'category')

    list_filter = ('author', 'category')
    search_fields = ("name","author__full_name", "category__name")
    ordering = ("created_at",)

    inlines = [FileBookInline, ]



admin.site.register(Book, BookAdmin)

admin.site.register(BookRead)

