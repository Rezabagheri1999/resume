from django.urls import path
from .views import social_network

urlpatterns = [
    path('social',social_network)
]