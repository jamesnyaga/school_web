from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from .models import Student
from .forms import StudentRegistration, StudentsProfileUpdateForm, StudentUpdateForm, StudentsUpdateForm

def studentsregister(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            student = form.save()
            student_username = student.username
            # Add user to the Students group
            students_group, created = Group.objects.get_or_create(name='Students')
            students_group.user_set.add(student)
            student.is_staff = False
            student.is_superuser = False
            student.save()
            messages.success(request, f'Account for {student_username} has been created. You are now able to log in.')
            return redirect('login')
    else:
        form = StudentRegistration()
    return render(request, 'students/students_register.html', {'form': form})

@login_required
def StudentProfile(request):
    student = getattr(request.user, 'student', None)
    try:
        profile = request.user.student
    except ObjectDoesNotExist:
        return render(request, 'students/error.html')
    
    # Query related objects
    grades = profile.subject_grades.all()
    average_grades = profile.average_grades.all()
    assignments = profile.assignments.all()
    #resources = profile.resource.all()
    comments = profile.comments.all()

    context = {
        'student':student,
        'grades': grades,
        'assignments':assignments,
        'average_grades': average_grades,
        'comments': comments,
    }
    return render(request, 'students/students_profile.html', context)



@login_required
def StudentProfile_edit(request):
    student = getattr(request.user, 'student',None)
    if not student:
        return render(request, 'students/error.html')
    
    if request.method == 'POST':
        u_form = StudentsUpdateForm(request.POST, instance = student.user)
        p_form = StudentsProfileUpdateForm(request.POST, request.FILES, instance=student.profile)
        s_form = StudentUpdateForm(request.POST, instance=student)

        if u_form.is_valid() and p_form.is_valid() and s_form.is_valid():
            u_form.save()
            p_form.save()
            s_form.save()
            messages.success(request, f'Account for {student.full_name} update successifully')
            return redirect('students-profile')
    else:
        u_form = StudentsUpdateForm(instance=request.user)
        p_form = StudentsProfileUpdateForm(instance=student.profile)
        s_form = StudentUpdateForm(instance=student)
    context = {
        'student':student,
        'u_form':u_form,
        'p_form':p_form,
        's_form':s_form
    }
    return render(request, 'students/students_profile_edit.html', context)



@login_required
def download_results(request):
    student = getattr(request.user, 'student', None)
    if not student:
        return render(request, 'students/error.html')
    student_profile = request.user.student
    grades = student_profile.subject_grades.all()
    average_grades = student_profile.average_grades.all()

    context = {
        'profile': student_profile,
        'grades': grades,
        'average_grades': average_grades,
    }

    # Render the HTML template with the context
    html_string = render_to_string('students/pdf_results.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="results.pdf"'

    # Convert HTML to PDF using xhtml2pdf
    result = BytesIO()
    pdf_status = pisa.CreatePDF(BytesIO(html_string.encode("UTF-8")), dest=result)
    
    # Check if there were any errors
    if pdf_status.err:
        return HttpResponse('Error generating PDF', status=500)
    
    response.write(result.getvalue())
    return response