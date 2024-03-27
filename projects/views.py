from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Task
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required
@require_http_methods(["GET"])
def monthly_tasks(request):
    # Get the user ID from the request parameters
    user_id = request.GET.get('user_id')

    # Get the current month
    current_month = datetime.now().month

    # Query the Task model to get all tasks for the given user ID and current month
    tasks = Task.objects.filter(empID=user_id, project_id__project_start_date__month=current_month)

    # Serialize the tasks
    serialized_tasks = [
        {"task_id": task.task_id, "task_name": task.task_name, "task_description": task.task_description,
         "time_required": task.time_required, "task_completion": task.task_completion} for task in tasks]

    # Return the serialized tasks in the HTTP response
    return JsonResponse(serialized_tasks, safe=False)
