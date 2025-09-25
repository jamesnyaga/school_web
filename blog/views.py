from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import BlogPosts
from parents.models import Parent
from teachers.models import Teacher
# Create your views here.
def Post_list(request):
	posts = BlogPosts.objects.all().order_by('-date_posted')
	context = {
		'posts':posts
	}
	return render(request, 'blog/blog_posts.html',context)
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













def home(request):
	return render(request, 'blog/home.html')

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