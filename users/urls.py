from django.urls import path


from .views import *


urlpatterns = [
    # path('current_user_participant', Current_User_Participant),
    path('register', RegisterUser),
    path("login", Login, name="user-login"),
    path("profile", user_data),
]