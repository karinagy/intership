from django.contrib import admin

# Register your models here.
from purchaser.models import Purchaser, Balance


class PurchaserAdmin(admin.ModelAdmin):
    search_fields = ['first_name__istartswith']
    ordering = ['-first_name']
    list_display = ['first_name', 'second_name', 'email', 'time_create']


class BalanceAdmin(admin.ModelAdmin):
    search_fields = ['value__istartswith']
    ordering = ['-value']
    list_display = ['purchaser', 'value']


admin.site.register(Purchaser, PurchaserAdmin)
admin.site.register(Balance, BalanceAdmin)
