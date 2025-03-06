from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Athlete, School

class UserRegistrationform(UserCreationForm):
    USER_TYPES = (
        ('athlete', 'Athlete'),
        ('school', 'School'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPES)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

class Athleteform(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['first_name','last_name','age','school_name','place']  # Replace with your actual fields

class Schoolform(forms.ModelForm):
    class Meta:
        model = School
        fields = ['person_name','school_name','place','phone_number','email']  # Replace with your actual fields
    