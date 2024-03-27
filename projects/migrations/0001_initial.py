<<<<<<< HEAD
# Generated by Django 5.0.2 on 2024-03-27 14:57
=======
# Generated by Django 5.0.3 on 2024-03-27 14:55
>>>>>>> cbc607f87935083ff21dcc6cc2bff5d01f2fa79b

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("project_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("project_team_size", models.IntegerField()),
                ("project_start_date", models.DateField()),
                ("project_end_date", models.DateField()),
                (
                    "empID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_related",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "Project",
                "ordering": ["project_id"],
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                ("task_id", models.AutoField(primary_key=True, serialize=False)),
                ("task_description", models.TextField()),
                ("task_name", models.CharField(max_length=100)),
                ("time_required", models.IntegerField()),
                ("task_completion", models.BooleanField(default=False)),
                (
                    "empID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_related",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.project",
                    ),
                ),
            ],
        ),
    ]
