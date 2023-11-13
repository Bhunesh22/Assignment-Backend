from django.contrib import admin
from .models import HistoriclaData

class UserAdmin(admin.ModelAdmin):
    search_fields = ['instrument_name', 'price', 'date', 'index']
    list_display = ['instrument_name', 'price', 'date', 'index']
    list_filter= ['instrument_name']

admin.site.register(HistoriclaData,UserAdmin)
