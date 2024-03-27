from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            group_name = form.cleaned_data.get('group')
            
            group, created = Group.objects.get_or_create(name=group_name)
            
            user.groups.add(group)
            
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})