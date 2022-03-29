from django.contrib import admin

# Register your models here.
from .models import Cars, Raiting, Rewiew, Car_dealership


class CarsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'curenncy', 'year', 'cat']
    list_editable = ['price', 'curenncy', 'year', 'cat']
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


admin.site.register(Cars, CarsAdmin)
admin.site.register(Raiting, RaitingAdmin)
admin.site.register(Rewiew)
admin.site.register(Car_dealership, Car_dealershipAdmin)
