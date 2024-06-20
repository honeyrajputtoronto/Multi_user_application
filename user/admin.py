from django.contrib import admin
from .models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['name','email','is_active','is_staff','is_realtor']
    search_fields = ('email', 'name')
    list_filter = ('is_active', 'is_staff', 'is_realtor')
    
    
admin.site.register(UserAccount, UserAccountAdmin)