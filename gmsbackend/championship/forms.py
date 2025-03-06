from django import forms
from userapp.models import Athlete, School

class AthleteRegistrationForm(forms.ModelForm):
    sports = forms.MultipleChoiceField(choices=[('swimming', 'Swimming'), ('badminton', 'Badminton')], widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Athlete
        fields = ['school_name', 'place', 'sports']


class SchoolRegistrationForm(forms.ModelForm):
    individual_sports = forms.MultipleChoiceField(choices=[('swimming', 'Swimming'), ('badminton', 'Badminton')], widget=forms.CheckboxSelectMultiple)
    team_sports = forms.MultipleChoiceField(choices=[('basketball', 'Basketball'), ('football', 'Football')], widget=forms.CheckboxSelectMultiple)
    num_students_individual = forms.IntegerField(min_value=0, label="Number of students in individual sports")
    num_students_team = forms.IntegerField(min_value=0, label="Number of students in team sports")

    class Meta:
        model = School
        fields = ['num_students_individual', 'num_students_team', 'individual_sports', 'team_sports']