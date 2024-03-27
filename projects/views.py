from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from projects.models import Task
from django.contrib.auth.decorators import login_required

'''
client = OpenAI(api_key='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')
system_prompt = "As the project manager for our software development project, I need assistance in task assignment. Below are the project details, and time constraint. Please provide task assignments for the project requirements.:"
end_prompt = "Provide an exhaustive list of tasks that need to be done in order to complete this project in the given time frame. The output apart from being in weeks have to be very precise and in details for each task so that they can be given to team members, I don't need you to split them to team members but I need you to make them very in detail so I can divide tasks for people. I also need them to be divided into each day of each week but each week has 5 working days."


def task_assignment(request):
    if request.method == 'POST':
        user_prompt = request.POST['user_prompt']
        final_prompt = system_prompt + user_prompt + end_prompt
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": final_prompt
            }],
        )
        return render(request, 'task_assignment.html', {'response': response})
'''

@login_required
def project_tasks(request, project_id):
    # Query the Task model to get all tasks for the given project ID
    tasks = Task.objects.filter(project_id=project_id)

    # Serialize the tasks
    serialized_tasks = [{"task_id": task.task_id, "task_name": task.task_name, "task_description": task.task_description, "time_required": task.time_required, "task_completion": task.task_completion} for task in tasks]

    # Pass the serialized tasks as context to the template
    context = {'tasks': serialized_tasks}
    return render(request, 'calendarPage.html', context)