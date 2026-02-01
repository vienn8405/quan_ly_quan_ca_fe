from django.contrib import admin
from .models import CafeShop
# Register your models here.
@admin.register(CafeShop)
class CafeShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'address')