from django.urls import path
from .views import add_like, find_recs

urlpatterns = [
    path('add_like/<int:id>', add_like),
    path('findrecommendations/<str:location>/<int:budget>/<str:term>/<int:ids>', find_recs),
]
