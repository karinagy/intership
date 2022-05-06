from django.contrib import admin

# Register your models here.
from .models import Car, Raiting, Review, Car_dealership, Car_dealershipSelling, Car_dealershipSeasonsales, \
    Car_m2m_Dealer


class CarAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'currency', 'year', 'cat']
    list_editable = ['price', 'currency', 'year', 'cat']
    ordering = ['-price', '-title']
    list_per_page = 8
    search_fields = ['title__istartswith']


class RaitingAdmin(admin.ModelAdmin):
    list_display = ['car', 'value']
    list_editable = ['value']
    search_fields = ['value__istartswith']
    ordering = ['-value']


class Car_dealershipAdmin(admin.ModelAdmin):
    search_fields = ['characteristic']
    ordering = ['-name']
    list_display = ['name', 'location', 'contact', 'is_published']


class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['purchaser']
    list_display = ['name', 'email', 'car']


class Car_dealershipSellingAdmin(admin.ModelAdmin):
    search_fields = ['car', 'car_dealership']
    ordering = ['-car']
    list_display = ['car', 'price', 'sale', 'time_create']


class Car_dealershipSeasonsalesAdmin(admin.ModelAdmin):
    search_fields = ['car', 'car_dealership']
    ordering = ['-car']
    list_display = ['car', 'first_price', 'sale', 'start_time', 'end_time']


class Car_m2m_DealerAdmin(admin.ModelAdmin):
    ordering = ['-autoshop']
    list_display = ['car', 'autoshop']


admin.site.register(Car, CarAdmin)
admin.site.register(Raiting, RaitingAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Car_dealership, Car_dealershipAdmin)
admin.site.register(Car_dealershipSelling, Car_dealershipSellingAdmin)
admin.site.register(Car_dealershipSeasonsales, Car_dealershipSeasonsalesAdmin)
admin.site.register(Car_m2m_Dealer, Car_m2m_DealerAdmin)
