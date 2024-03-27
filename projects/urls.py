from django.urls import path
from .views import monthly_tasks

urlpatterns = [
    path('monthly_tasks/<int:course_id>', monthly_tasks, name='monthly_tasks'),
]