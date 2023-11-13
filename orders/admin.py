from django.contrib import admin
from .models import Orders

class UserAdmin(admin.ModelAdmin):
    search_fields = ['user','tradingsymbol', 'exchange', 'quantity', 'average_price', 'last_price', 'close_price']
    list_display = ['user','tradingsymbol', 'exchange', 'quantity', 'average_price', 'last_price', 'close_price']
    list_filter= ['tradingsymbol', 'exchange']

admin.site.register(Orders,UserAdmin)
