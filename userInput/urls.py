from django.urls import path
from .views import create_hangout, view_hangout, submit_budget, final_budget

urlpatterns = [
    path('create_hangout/', create_hangout),
    path('view_hangout/<int:group_id>', view_hangout),
    path('submit_budget/<int:group_id>', submit_budget),
    path('final_budget/<int:hangout_id>', final_budget),

]
