from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as Admin

# Register your models here.
class UserAdmin(Admin):
    model = User
    list_display = ("email", "username", "is_staff", "is_active", "is_superuser")
    fieldsets = (
        ("Personal", {"fields": ("email", "username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        ("Personal", {
            "classes": ("wide",),
            "fields": (
                "email", "username", "password1", "password2"
            )}
         ),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    list_filter = ()
    search_fields = ("email", "username")
    ordering = ("email",)

admin.site.register(User, UserAdmin)