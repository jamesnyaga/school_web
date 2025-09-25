from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from .forms import TeachersCreationForm,TeachersProfileUpdateForm, TeachersUpdateForm, TeacherUpdateForm, Tr_StudentAssignmentUpdateForm, Tr_StudentAverageGradeUpdateForm, Tr_StudentClassTeachersCommentUpdateForm, Tr_StudentProfileUpdateForm, Tr_StudentresourcesUpdateForm,Tr_StudentSubjectGradeUpdateForm,ClassTeachersComment, Tr_StudentUpdateForm,Tr_StudentsUpdateForm
from.models import Teacher
from students.models import Student, Profile

# Create your views here.
@login_required
def TeachersProfile(request):
    teacher = getattr(request.user, 'teacher', None)

    if not teacher:
        return render(request, 'teachers/error.html')
    
    students = Student.objects.filter(student_class=teacher.class_teacher)
    context = {
        'students':students,
        'profile':Profile,
        'teacher':teacher,
    }

    return render(request, 'teachers/teachers_profile.html', context)

@login_required
def teacher_profile_update(request):
    teacher = getattr(request.user, 'teacher', None)
    if not teacher:
        return render(request, 'teachers/error.html')
    if request.method == 'POST':
        p_form = TeachersProfileUpdateForm(request.POST,request.FILES,instance=teacher.profile)
        u_form = TeachersUpdateForm(request.POST, instance=request.user)
        t_form =  TeacherUpdateForm(request.POST, instance=teacher)
        if u_form.is_valid() and p_form.is_valid() and t_form.is_valid():
            u_form.save()
            p_form.save()
            t_form.save()
            messages.success(request, 'your profile has been updated successiful!')
            return redirect('teachers-profile')
    else:
        p_form = TeachersProfileUpdateForm(instance=teacher.profile)
        u_form = TeachersUpdateForm(instance=request.user)
        t_form =  TeacherUpdateForm(instance=teacher)
    
    context = {
        'teacher':teacher,
        'u_form':u_form,
        'p_form':p_form,
        't_form':t_form
    }

    return render(request,'teachers/profile_update.html', context)

@login_required
def update_student_info(request, student_id):
    teacher = getattr(request.user, 'teacher', None)
    student = get_object_or_404(Student, id =student_id)
    if not teacher:
        return render(request, 'teachers/error.html')
    
    if request.method == 'POST':
        student_form = Tr_StudentUpdateForm(request.POST, instance=student)
        student_u_form = Tr_StudentsUpdateForm(request.POST, instance=student.user)
        assignment_form = Tr_StudentAssignmentUpdateForm(request.POST, instance=student.assignments.first())
        grade_form = Tr_StudentAverageGradeUpdateForm(request.POST, instance=student.average_grades.first())
        subject_grade_form = Tr_StudentAverageGradeUpdateForm(request.POST,instance=student.subject_grades.first())
        comment_form = Tr_StudentClassTeachersCommentUpdateForm(request.POST, instance=student.comments.first())
        resource_form = Tr_StudentresourcesUpdateForm(request.POST, instance=student.resources.first())
        profile_form = Tr_StudentProfileUpdateForm(request.POST, request.FILES, instance=student.profile)
        if all([student_form.is_valid(),student_u_form.is_valid(), assignment_form.is_valid(),resource_form.is_valid(),grade_form.is_valid(),subject_grade_form.is_valid(),comment_form.is_valid(),profile_form.is_valid()]):
            student_form.save()
            student_u_form.save()
            assignment_form.save()
            grade_form.save()
            subject_grade_form.save()
            comment_form.save()
            resource_form.save()
            profile_form.save()
            messages.success(request, f'{student.full_name} profile has been updated successifull!')
            return redirect('teachers-profile')
    else:
        student_form = Tr_StudentUpdateForm(instance=student)
        student_u_form = Tr_StudentsUpdateForm(instance=student.user)
        assignment_form = Tr_StudentAssignmentUpdateForm(instance=student.assignments.first())
        grade_form = Tr_StudentAverageGradeUpdateForm(instance=student.average_grades.first())
        subject_grade_form = Tr_StudentSubjectGradeUpdateForm(instance=student.subject_grades.first())
        comment_form = Tr_StudentClassTeachersCommentUpdateForm(instance=student.comments.first())
        resource_form = Tr_StudentresourcesUpdateForm(instance=student.resources.first())
        profile_form = Tr_StudentProfileUpdateForm(request.FILES, instance=student.profile)

    context ={
        'student':student,
        'teacher': teacher,
        'student_u_form':student_u_form,
        'student':student,
        'student_form':student_form,
        'assignment_form':assignment_form,
        'grade_form':grade_form,
        'subject_grade_form':subject_grade_form,
        'comment_form':comment_form,
        #'resource_form':resource_form,
        'profile_form':profile_form 
    }
    return render(request, 'teachers/student_profile_update.html',context)

"""def TeacherRegister(request):
    if request.method == 'POST':
        form = TeachersCreationForm(request.POST)
        if form.is_valid():
            teacher = form.save
            teacher_username = teacher.username
            Username = form.cleaned_data.get('username')
            teacher.save()
            messages.success(request, f'Account created for {Username}!')
            return redirect('teachers-profile')
    else:
        form = TeachersCreationForm()
    return render(request, 'teachers/register.html', {'form':form})
"""
    
def TeacherRegister(request):
    if request.method == 'POST':
        form = TeachersCreationForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            teacher_username = teacher.username
            # Add user to the Teachers group
            teacher_group, created = Group.objects.get_or_create(name='Teacher')
            teacher_group.user_set.add(teacher)
            # Set permissions
            teacher.is_staff = False
            teacher.is_superuser = True
            # Create the Teacher profile
            Teacher.objects.create(
                user = teacher,
                username = teacher_username,
                full_name = form.cleaned_data.get('full_name'),
                tr_description="I am a passionate teacher with a love for guiding and inspiring students. My goal is to create an engaging and supportive learning environment where everyone can thrive."
            )
            teacher.save()
            messages.success(request, f'Account for {teacher_username} has been created.You are now able to log in. please after you login navigate to /admin and fill in the empty data')
            return redirect('login')
    else:
        form = TeachersCreationForm()
    return render(request, 'teachers/register.html', {'form':form})
