from django.urls import path, include
from blog import views as blog_views
from school import views as school_views

urlpatterns = [

    path('', blog_views.home, name='school-home'),

    path('gallery/', school_views.gallery_display, name='gallery'),

    path('blog/', include('blog.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('parents/', include('parents.urls')),

]