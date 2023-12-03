from django.urls import path
from .views import orders

urlpatterns = [
    path('order', orders)
]
