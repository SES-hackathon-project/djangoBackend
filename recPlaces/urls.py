from django.urls import path
from .views import add_like

urlpatterns = [
    path('add_like/<str:name>', add_like),
]
