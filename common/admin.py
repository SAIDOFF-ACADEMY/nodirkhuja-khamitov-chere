from django.contrib import admin
from django.http import HttpRequest

from .model.page import Page
from .model.setting import Setting
from .model.contact import UserContact
from .model.free_product import FreeProduct
from .model.page import Page

admin.site.register(Page)
admin.site.register(FreeProduct)
admin.site.register(UserContact)


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