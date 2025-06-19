from django.urls import path
from barbearia.views import my_view, sobre, home

urlpatterns = [
    path('my-view/', my_view),
    path('sobre/', sobre),
    path('home/', home)
]