from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group, User
from .models import Parent, Profile
from students.models import Student
from .forms import ParentCreationForm, ParentsUpdateForm, ParentUpdateForm,ParentProfileUpdateForm

# Create your views here.
def parents_register(request):
    if request.method == 'POST':
        form = ParentCreationForm(request.POST)
        if form.is_valid():
            #extracting the data
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            full_name = form.cleaned_data.get('full_name')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            contact = form.cleaned_data.get('contact')
            My_Student_Adm_No = form.cleaned_data.get('My_Student_Adm_No')
            #create the user
            parent_user = User.objects.create_user(username=username, email=email, password=password1)
            parent_user.is_staff = False
            parent_user.is_superuser = False
            try:
                student = Student.objects.get(student_id =My_Student_Adm_No)
            except Student.DoesNotExist:
                messages.error(request,'Student with this admission number does not exist')
                comit = False
                return redirect('parents-register')
            
            parents_group, created= Group.objects.get_or_create(name='Parents')
            parents_group.user_set.add(parent_user)
            #create the parents profile
            Parent.objects.create(
                user=parent_user,
                username = parent_user.username,
                full_name = form.cleaned_data.get('full_name'),
                contact = form.cleaned_data.get('contact'),
                My_Student_Adm_No = student
            )
            parent_user.save()
            messages.success(request, f'Account created for {parent_user.username} has been created successifully you are now able to login')
            return redirect('login')
    else:
        form = ParentCreationForm()
    context = {
        'form':form
    }
    return render(request, 'parents/register.html', context)

@login_required
def ParentsProfile(request):
    parent = getattr(request.user, 'parent',None)
    if not parent:
        return redirect(request, 'parents/parents_error.html')
    student = parent.My_Student_Adm_No if parent.My_Student_Adm_No else None
    context = {
        'parent':parent,
        'student':student,
    }
    return render(request, 'parents/parents_profile.html',context)

@login_required
def ParentsProfileUpdate(request):
    parent = getattr(request.user, 'parent', None)
    if not parent:
        return render(request, 'parents/parents_error.html')
    if request.method == 'POST':
        u_form = ParentsUpdateForm(request.POST, instance=request.user)
        pr_form = ParentUpdateForm(request.POST, instance=parent)
        p_form = ParentProfileUpdateForm(request.POST, request.FILES, instance=parent.profile)
        if all([u_form.is_valid(), pr_form.is_valid(), p_form.is_valid()]):
            u_form.save()
            pr_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated successifuly!')
            return redirect('parents-profile')
    else:
        u_form = ParentsUpdateForm(instance=request.user)
        pr_form = ParentUpdateForm(instance=parent)
        p_form = ParentProfileUpdateForm(instance=parent.profile)
    context = {
        'parent':parent,
        'u_form':u_form,
        'pr_form':pr_form,
        'p_form':p_form
    }

    return render(request, 'parents/profile_update.html', context)



@login_required
def pr_StudentProfile(request, student_id):
    profile = getattr(request.user, 'student', None) or getattr(request.user, 'parent', None)
    s_profile = get_object_or_404(Student, id=student_id)

    if not profile:
        return render(request, 'students/error.html')
    
    if profile == getattr(request.user, 'parent', None):
        if s_profile != profile.My_Student_Adm_No:
            messages.error(request,'You do not have permission to view this student profile!')
            return render(request, 'students/error.html')
    
    # Query related objects
    grades = s_profile.subject_grades.all()
    average_grades = s_profile.average_grades.all()
    assignments = s_profile.assignments.all()
    #resources = s_profile.resource.all()
    comments = s_profile.comments.all()

    context = {
        'student':s_profile,
        'profile': profile,
        'grades': grades,
        'average_grades': average_grades,
        'comments': comments,
    }
    return render(request, 'parents/my_students_profile.html', context)

