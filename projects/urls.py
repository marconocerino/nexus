from django.urls import path
from .views import project_tasks

urlpatterns = [
    path('project_tasks/<int:project_id>', project_tasks, name='project_tasks'),
]