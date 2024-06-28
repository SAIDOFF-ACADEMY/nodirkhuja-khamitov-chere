from django.contrib import admin
from django.http import HttpRequest

from .model.page import Page
from .model.setting import Setting

admin.site.register(Page)

@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    

    def has_delete_permission(self, request, obj=None) -> bool:
        return False
    
    def has_add_permission(self, request) -> bool:
        exist = Setting.objects.exists()
        if exist:
            return False
        else:
            return True