from django.urls import path
from .views import cafe_map

urlpatterns = [
    path('map/', cafe_map, name='cafe_map'),
]