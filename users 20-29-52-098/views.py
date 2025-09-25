from django.shortcuts import render, redirect
from students .models import Student, Profile
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    student = getattr(request.user, 'student', None)
    teacher = getattr(request.user, 'teacher', None)
    parent = getattr(request.user, 'parent', None)

    context = {
            'teacher':teacher,
            'student':student,
            'parent':parent
        }
    
    return render(request, 'users/profile.html', context)

@login_required
def profile_redirect(request):
    user = request.user
    if user.is_student:
        return redirect('student-profile')
    elif user.is_teacher:
        return redirect('teacher-profile')
    else:
        return redirect('default-profile')
