from django.contrib import admin

# Register your models here.
from .models import Car, Raiting, Rewiew, Car_dealership


class CarAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'currency', 'year', 'cat']
    list_editable = ['price', 'currency', 'year', 'cat']
    ordering = ['-price', '-title']
    list_per_page = 3
    search_fields = ['title__istartswith']


class RaitingAdmin(admin.ModelAdmin):
    list_display = ['car', 'value']
    list_editable = ['value']
    search_fields = ['value__istartswith']
    ordering = ['-value']


class Car_dealershipAdmin(admin.ModelAdmin):
    search_fields = ['characteristic']
    ordering = ['-name']


class RewiewAdmin(admin.ModelAdmin):
    search_fields = ['purchaser']
    list_display = ['name', 'email', 'car']


admin.site.register(Car, CarAdmin)
admin.site.register(Raiting, RaitingAdmin)
admin.site.register(Rewiew, RewiewAdmin)
admin.site.register(Car_dealership, Car_dealershipAdmin)
