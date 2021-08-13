from django.urls import path
from .views import add_like, find_recs

urlpatterns = [
    path('add_like/<str:name>', add_like),
    path('findrecommendations/<str:location>/<str:budget>/<str:term>/<int:ids>', find_recs),
]
