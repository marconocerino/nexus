from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Count
from courses.models import Course, Tag


class CustomUser(AbstractUser):
    # 'username', 'email', 'first_name', 'last_name', 'password' fields are already part of AbstractUser

    def recommend_courses(self):
        # Fetch user's enrolled courses
        enrolled_courses = Course.objects.filter(students=self)

        # Get tags from those courses
        tags = Tag.objects.filter(courses__in=enrolled_courses).distinct()

        # Recommend courses that share the same tags and are not already enrolled by the user
        recommended_courses = Course.objects.filter(tags__in=tags).exclude(students=self).distinct()

        return recommended_courses
