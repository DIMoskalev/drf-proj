from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email")
    search_fields = ("id", "email")
    list_display = ("id", "email", "is_staff", "is_active")
