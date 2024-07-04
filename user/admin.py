from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserContactApplication

class UserAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'full_name', 'phone_number', 'language', 'created_at')
    readonly_fields = ['created_at',]

admin.site.register(User, UserAdmin)
admin.site.register(UserContactApplication)
