from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def login_signup_view(request):
    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'signup':
            signup_form = CustomUserCreationForm(request.POST)
            login_form = AuthenticationForm()
            if signup_form.is_valid():
                signup_form.save()
                # Optionally, you might want to log the user in directly after signup
                user = authenticate(username=signup_form.cleaned_data['username'],
                                    password=signup_form.cleaned_data['password1'])
                if user:
                    login(request, user)
                return redirect('home')
        elif 'action' in request.POST and request.POST['action'] == 'login':
            login_form = AuthenticationForm(request, data=request.POST)
            signup_form = CustomUserCreationForm()
            if login_form.is_valid():
                # Log in the user
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                if user:
                    login(request, user)
                    return redirect('home')
    else:
        signup_form = CustomUserCreationForm()
        login_form = AuthenticationForm()

    return render(request, 'login.html', {'signup_form': signup_form, 'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('home')
