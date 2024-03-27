from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import Group

class CustomUserCreationForm(UserCreationForm):
    SEX_CHOICES = [
        ('', '---------'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non-Binary'),
        ('PNS', 'Preferred Not to Say'),
    ]

    ROLE_CHOICES = [
        ('', '---------'),
        ('EMPLOYEE', 'Employee'),
        ('MANAGER', 'Manager'),
    ]

    age = forms.IntegerField(required=False)
    sex = forms.ChoiceField(choices=SEX_CHOICES, required=False)
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=False)
    location = forms.CharField(max_length=100, required=False)
    department = forms.CharField(max_length=100, required=False)


    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'sex', 'role', 'location', 'department')

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age < 0:
            raise forms.ValidationError("Age cannot be negative.")
        return age
