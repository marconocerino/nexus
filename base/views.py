from django.shortcuts import render
from django.views.generic import TemplateView
from projects.models import Project

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


class CalendarView(TemplateView):
    template_name = 'calendar.html'


def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def another_view(request):
    projects = Project.objects.all()
    
    return render(request, 'calendar.html', {'projects': projects})

