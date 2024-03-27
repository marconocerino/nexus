from django.shortcuts import render
import os
from dotenv import load_dotenv, dotenv_values
from openai import OpenAI
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from projects.models import Task
from django.contrib.auth.decorators import login_required
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
system_prompt = "As the project manager for our software development project, I need assistance in task assignment. Below are the project details, and time constraint. Please provide task assignments for the project requirements.:"
user_prompt=""
end_prompt = "Please provide in detail each task assignment for the team member and "
final_prompt = system_prompt + user_prompt
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
            "role": "user",
            "content": final_prompt
        }],
)


@login_required
def project_tasks(request, project_id):
    # Query the Task model to get all tasks for the given project ID
    tasks = Task.objects.filter(project_id=project_id)

    # Serialize the tasks
    serialized_tasks = [{"task_id": task.task_id, "task_name": task.task_name, "task_description": task.task_description, "time_required": task.time_required, "task_completion": task.task_completion} for task in tasks]

<<<<<<< HEAD
    # Pass the serialized tasks as context to the template
    context = {'tasks': serialized_tasks}
    return render(request, 'calendarPage.html', context)
=======
    # Return the serialized tasks in the HTTP response
    return JsonResponse(serialized_tasks, safe=False)
    return render(request, 'calendarPage.html', serialized_tasks)

>>>>>>> cbc607f87935083ff21dcc6cc2bff5d01f2fa79b
