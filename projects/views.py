from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from projects.models import Task
from django.contrib.auth.decorators import login_required

@login_required
def project_tasks(request, project_id):
    # Query the Task model to get all tasks for the given project ID
    tasks = Task.objects.filter(project_id=project_id)

    # Serialize the tasks
    serialized_tasks = [{"task_id": task.task_id, "task_name": task.task_name, "task_description": task.task_description, "time_required": task.time_required, "task_completion": task.task_completion} for task in tasks]

    # Pass the serialized tasks as context to the template
    context = {'tasks': serialized_tasks}
    return render(request, 'calendarPage.html', context)