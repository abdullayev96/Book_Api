from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author_name', 'comment','answers', 'status', 'user')

    list_filter = ('book_name', 'author_name')
    search_fields = ("book_name",)


admin.site.register(Order, OrderAdmin)
