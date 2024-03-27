
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from courses.models import Course

class CourseInline(admin.TabularInline):
    model = Course.students.through
    extra = 1

class CustomUserAdmin(UserAdmin):
    inlines = [CourseInline, ]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)

