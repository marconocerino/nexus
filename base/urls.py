from django.urls import path
from . import views
from .views import HomePageView, CalendarView

app_name = 'nexus'

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('calendar/', CalendarView.as_view(), name='calendar'),
]

