from django.urls import path
from .views import essaies

urlpatterns = [
    path('essay', essaies)
]
