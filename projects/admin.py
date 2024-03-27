from django.contrib import admin
from .models import Project, Task

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'name', 'project_team_size', 'project_start_date', 'project_end_date', 'empID']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_id', 'project_id', 'task_name', 'task_description', 'time_required', 'task_completion', 'empID']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
