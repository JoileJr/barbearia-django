from django.urls import path
from barbearia.views import my_view, sobre

urlpatterns = [
    path('my-view/', my_view),
    path('sobre/', sobre),
]