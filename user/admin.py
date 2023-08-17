from django.contrib import admin
from .models import *

# Register your models here

class UserAdmin(admin.ModelAdmin):

    readonly_fields=('date_joined','updatedAt', 'password')
    list_display = ['full_name', 'phone', 'is_staff', 'is_active', 'is_verified', 'date_joined', 'updatedAt']

    search_fields = ['full_name', 'last_name', 'phone']
    
    list_filter = ['is_staff', 'is_active', 'is_verified', 'date_joined']


class SmsAdmin(admin.ModelAdmin):
    readonly_fields=('sms',)
    list_display = ['phone', 'sms']
    search_fields = ['phone']
    
admin.site.register(User, UserAdmin)
admin.site.register(Sms, SmsAdmin)
