from django.urls import path
from .views import create_hangout, view_hangout, submit_budget

urlpatterns = [
    path('create_hangout/', create_hangout),
    path('view_hangout/<int:group_id>', view_hangout),
    path('submit_budget/<int:groupd_id>', submit_budget),
]
