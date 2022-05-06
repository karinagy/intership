from django.contrib import admin

# Register your models here.
from .models import Supplier, Founder, Raiting


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_of_purchasers']
    list_per_page = 5
    ordering = ['-number_of_purchasers']
    search_fields = ['name__istartswith']


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Founder)
admin.site.register(Raiting)

