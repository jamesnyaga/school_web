from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import BlogPosts
from parents.models import Parent
from teachers.models import Teacher
from school.models import School, Gallery
# Create your views here.
def Post_list(request, school_slug):
    user = request.user

    if hasattr(user, 'teacher'):
        school = user.teacher.school
    elif hasattr(user, 'student'):
        school = user.student.school
    elif hasattr(user, 'parent'):
        school = user.parent.school
    else:
        # fallback to EDUROLLING if no profile
        school = School.objects.get(code='EDU001')

    # Filter posts by the user's school
    school = get_object_or_404(School, slug=school_slug)
    posts = BlogPosts.objects.filter(school=school).order_by('-date_posted')

    context = {'posts': posts, 'school':school}
    return render(request, 'blog/blog_posts.html', context)

def get_profile_pic(self):
	if hasattr(self, 'parent'):
		return self.parent.profile.image.url
	elif hasattr(self, 'teacher'):
		return self.teacher.profile.image.url
	else:
		return self.profile.image.url if hasattr(self, 'profile')else 'media/parents_default_image.jpg'
User.add_to_class('get_profile_pic',get_profile_pic)

def PostDetails(request, id):
	post = get_object_or_404(BlogPosts, id=id)
	context = {
		'post':post
	}
	return render(request, 'blog/blog_detail.html', context)

def latestPosts(request):
	return render(request, 'blog/latest_posts.html')





def home(request, school_slug=None):
    # If school_code is None, fallback to EDUROLLING
    if school_slug:
        school = get_object_or_404(School, slug=school_slug.lower())  # school codes are uppercase
    else:
        school = School.objects.get(code='EDU001')  # EDUROLLING default

    gallery_images = Gallery.objects.filter(school=school)
    posts = BlogPosts.objects.filter(school=school).order_by('-date_posted')

    context = {
        'school': school,
        'gallery_images': gallery_images,
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)





def about(request):
	return render(request, 'blog/about.html')

def Academics(request):
	return render(request, 'blog/academics.html')

def Admission(request):
	return render(request, 'blog/admission.html')

def Student_lifes(request):
	return render(request, 'blog/student_lifes.html')

def Gallerly(request):
	return render(request, 'blog/gallerly.html')

    

def login(request):
	return render(request, 'blog/login.html')

def announcements(request):
	return render(request, 'blog/announcements.html')

def calendars(request):
	return render(request, 'blog/calendars.html')

def Others(request):
	return render(request, 'blog/others.html')