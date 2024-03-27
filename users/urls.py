from django.urls import path
from django.contrib.auth import views as auth_views
from .views import profile_view, login_signup_view

app_name = 'users'

urlpatterns = [
    path('login-signup/', login_signup_view, name='login_signup'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user_pages/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='user_pages/password_change_done.html'), name='password_change_done'),
    path('profile/<str:username>/', profile_view, name='profile'),
]

