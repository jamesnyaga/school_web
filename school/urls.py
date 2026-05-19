from django.urls import path, include
from .import views
from blog.views import home
"""
urlpatterns = [
    path('gallery/', views.gallery_display, name='gallery'),
    path('gallery/add/', views.GalleryUpdate, name='gallery-add'),
    path('', views.home, name='school-home'),
    path('blog/', include('blog.urls')),
]
"""
urlpatterns = [
    # 🏠 SCHOOL HOME
    path('', home, name='school-home'),

    # 📸 Gallery
    path('gallery/', views.gallery_display, name='gallery'),

    # 📝 Blog
    path('blog/', include('blog.urls')),

    # 👨‍🎓 Students
    path('students/', include('students.urls')),

    # 👨‍🏫 Teachers
    path('teachers/', include('teachers.urls')),

    # 👨‍👩‍👧 Parents
    path('parents/', include('parents.urls')),

    path('academic/', include('academic.urls')),

]