from django.contrib import admin
from .models import Performer



class PerformerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'bio', 'photo')

    list_filter = ('full_name', 'bio')
    search_fields = ("full_name",)



admin.site.register(Performer, PerformerAdmin)
