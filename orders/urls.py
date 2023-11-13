from django.urls import path


from .views import *


urlpatterns = [
    path('portfolio/holdings', Holdings),
    path('order/place_order', Order_palce),
]