from django.db import models
from django.conf import settings


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    project_team_size = models.IntegerField()
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    empID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='project_related'  # changed related_name
    )

    class Meta:
        db_table = 'Project'
        ordering = ['project_id']

    def __str__(self):
        return self.project_id


class Task(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_id = models.AutoField(primary_key=True)
    empID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='task_related'  # changed related_name
    )
    task_description = models.TextField()
    task_name = models.CharField(max_length=100)
    time_required = models.IntegerField()
    task_completion = models.BooleanField(default=False)
