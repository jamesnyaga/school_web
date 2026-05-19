from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


"""
urlpatterns = [
    path('<slug:school_slug>/', views.home, name='school-home'),
    path('academics/', views.Academics, name='blog-academics'),
    path('admissions/', views.Admission, name='blog-admission'),
    path('student lifes/', views.Student_lifes, name='blog-student-life'),
    path('gallerly/', views.Gallery, name='blog-gallerly'),
    path('blog/', views.Post_list, name='blog-blogs'),
    path('login/', views.login, name='blog-login'),
    path('about/', views.about, name='blog-about'),
    path('announcements/', views.announcements, name='blog-announcements'),
    path('latest Posts/', views.latestPosts, name='blog-latestPosts'),
    path('calendars/', views.calendars, name='blog-calendars'),
    path('blog-detail/<int:id>/', views.PostDetails, name='blog-detail'), 
    path('etcs/', views.Others, name='blog-others'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_list, name='blog-home'),
    path('post/<int:id>/', views.PostDetails, name='blog-detail'),
    path('blog/', views.Post_list, name='blog-blogs'),

    path('academics/', views.Academics, name='blog-academics'),
    path('admissions/', views.Admission, name='blog-admission'),
    path('student-life/', views.Student_lifes, name='blog-student-life'),
    path('gallery/', views.Gallery, name='blog-gallery'),

    path('about/', views.about, name='blog-about'),
    path('announcements/', views.announcements, name='blog-announcements'),
    path('calendar/', views.calendars, name='blog-calendars'),
    path('latest/', views.latestPosts, name='blog-latest-posts'),
    path('etcs/', views.Others, name='blog-others'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)