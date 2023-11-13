from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', 'user_name', 'broker', 'user_type']
    list_display = ['email', 'user_name', 'broker', 'user_type']
    list_filter= ['broker', 'user_type']

admin.site.register(User,UserAdmin)
