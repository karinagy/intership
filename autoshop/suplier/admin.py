from django.contrib import admin

# Register your models here.
from .models import Suplier, Founder, Raiting


class SuplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'number_of_purchasers']
    list_per_page = 5
    ordering = ['-number_of_purchasers']
    search_fields = ['name__istartswith']


admin.site.register(Suplier, SuplierAdmin)
admin.site.register(Founder)
admin.site.register(Raiting)

