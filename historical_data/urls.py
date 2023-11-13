from django.urls import path


from .views import *


urlpatterns = [
    path('historical_price_data/', HistoricalPriceData),
    path('add_data', AddData),
]