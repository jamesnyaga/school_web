from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('academics/', views.Academics, name='blog-academics'),
    path('admissions/', views.Admission, name='blog-admissions'),
    path('student lifes/', views.Student_lifes, name='blog-student lifes'),
    path('gallerly/', views.Gallerly, name='blog-gallerly'),
    path('blog/', views.Post_list, name='blog-blogs'),
    path('login/', views.login, name='blog-login'),
    path('about/', views.about, name='blog-about'),
    path('announcements/', views.announcements, name='blog-announcements'),
    path('latest Posts/', views.latestPosts, name='blog-latestPosts'),
    path('calendars/', views.calendars, name='blog-calendars'),
    path('blog-detail/<int:id>/', views.PostDetails, name='blog-detail'), 
    path('etcs/', views.Others, name='blog-others'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
