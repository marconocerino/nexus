from django.urls import path
from . import views
from .views import HomePageView, CalendarView, projects_view, another_view

app_name = 'nexus'

urlpatterns = [
  path('calendar/', another_view, name="calendar"),
  path('', projects_view, name="home"),
]

