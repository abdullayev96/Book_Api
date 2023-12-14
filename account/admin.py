from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from rest_framework.authtoken.models import Token




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display  = ('username', 'email','password', 'is_staff', 'is_active')
    list_filter = ('username', 'email','password', 'is_staff', 'is_active')

    fieldsets = (
              (None, {"fields": ("username", "password")}),
              ("Permissions", {"fields": ("email", "is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
              (None, {
                        "classes": ("wide",),
                        "fields": (
                                  "username", "password1", "password2", "is_staff",
                                  "email", "is_active", "groups", "user_permissions"
                        )}
               ),
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Token)



