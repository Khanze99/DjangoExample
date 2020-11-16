from django.urls import path
from .views import get_view

urlpatterns = [
    path('example/', get_view),
]
