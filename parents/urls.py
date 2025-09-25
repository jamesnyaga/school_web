from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.parents_register, name='parents-register'),
    path('profile/', views.ParentsProfile, name='parents-profile'),
    path('profile_update/', views.ParentsProfileUpdate, name='parents-profile-update'),
    path('student_profile/<int:student_id>/', views.pr_StudentProfile, name='parent-student-profile'),
]