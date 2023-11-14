from django.urls import path


from .views import *


urlpatterns = [
    path('historical-data', HistoricalPriceData),
    path('add_data', AddData),
]