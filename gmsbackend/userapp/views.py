from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegistrationform, Athleteform, Schoolform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationform(request.POST)
        if user_form.is_valid():
            try:
                user = user_form.save(commit=False)  # First save user without committing
                user.save()  # Now save the user
                
                user_type = user_form.cleaned_data.get('user_type')
                
                if user_type == 'athlete':
                    athlete_form = Athleteform(request.POST)
                    if athlete_form.is_valid():
                        athlete = athlete_form.save(commit=False)
                        athlete.user = user
                        athlete.save()
                    else:
                        user.delete()  # Delete user if athlete form is invalid
                        messages.error(request, f"Athlete form errors: {athlete_form.errors}")
                        return render(request, 'userapp/register.html', {
                            'user_form': user_form,
                            'athlete_form': athlete_form,
                            'school_form': Schoolform()
                        })
                        
                elif user_type == 'school':
                    school_form = Schoolform(request.POST)
                    if school_form.is_valid():
                        school = school_form.save(commit=False)
                        school.user = user
                        school.save()
                    else:
                        user.delete()  # Delete user if school form is invalid
                        messages.error(request, f"School form errors: {school_form.errors}")
                        return render(request, 'userapp/register.html', {
                            'user_form': user_form,
                            'athlete_form': Athleteform(),
                            'school_form': school_form
                        })

                login(request, user)
                messages.success(request, "Registration successful!")
                return redirect('home')
            
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return render(request, 'userapp/register.html', {
                    'user_form': user_form,
                    'athlete_form': Athleteform(),
                    'school_form': Schoolform()
                })
        else:
            messages.error(request, f"Form validation errors: {user_form.errors}")
    else:
        user_form = UserRegistrationform()
        athlete_form = Athleteform()
        school_form = Schoolform()
    
    return render(request, 'userapp/register.html', {
        'user_form': user_form,
        'athlete_form': athlete_form,
        'school_form': school_form,
    })

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'userapp/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

@login_required
def home(request):
    return render(request, 'userapp/home.html')

