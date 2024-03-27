from django.urls import path
from .views import monthly_tasks

urlpatterns = [
    path('monthly_tasks/', monthly_tasks, name='monthly_tasks'),
]