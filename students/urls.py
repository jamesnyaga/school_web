from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.studentsregister, name='students-register'),
    path('profile/', views.StudentProfile, name='students-profile'),
    path('download-results/', views.download_results, name='download_results'),
    path('profile-edit/', views.StudentProfile_edit, name='profile_edit'),
]
