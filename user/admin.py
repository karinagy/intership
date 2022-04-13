from django.contrib import admin

# Register your models here.
from user.models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    ordering = ['-username']
    list_display = ['username', 'email', 'phone', 'date_joined']


admin.site.register(User, UserAdmin)
