from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from.models import Gallery
from school.models import School
from.forms import GalleryUpdateForm
from students .models import Student, Profile
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


@login_required
def gallery_display(request, school_slug=None):

    school = get_object_or_404(School, slug=school_slug)

    images = Gallery.objects.filter(school=school)

    return render(request, 'school/gallery.html', {
        'images': images,
        'school': school
    })

def super_user_require(view_func):
     def wrapper(request, *args, **kwargs):
          if not request.user.is_superuser:
               messages.error(request,'OOPS YOU DO NOT HAVE THE NECCESSARY PERMISSIONS TO VIEW THAT PAGE')
               return redirect('gallery')
          return view_func(request, *args, **kwargs)
     return wrapper
          
     #decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
     #return decorated_view_func

@super_user_require
def GalleryUpdate(request):
     if request.method == 'POST':
          g_form = GalleryUpdateForm(request.POST, request.FILES)
          if g_form.is_valid():
               g_form.save()
               messages.success(request, 'The image was added to gallery successifully!')
               return redirect ('gallery')
     else:
          g_form = GalleryUpdateForm(request.FILES)
     context = {
          'g_form':g_form
     }
     return render(request, 'school/gallery_update.html', context)


def register(request):
    school = School.objects.filter(code='EDU001').first()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'school/register.html', {
        'form': form,
        'school': school
    })

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
    
    return render(request, 'school/profile.html', context)




from django.shortcuts import redirect

def dashboard_redirect(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('login')

    try:
        return redirect('school-home', school_slug=user.student.school.slug)
    except:
        pass

    try:
        return redirect('school-home', school_slug=user.teacher.school.slug)
    except:
        pass

    try:
        return redirect('school-home', school_slug=user.parent.school.slug)
    except:
        pass

    # fallback
    return redirect('login')







@login_required
def profile_redirect(request):
    user = request.user
    if user.is_student:
        return redirect('student-profile')
    elif user.is_teacher:
        return redirect('teacher-profile')
    else:
        return redirect('default-profile')


