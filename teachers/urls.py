from django.urls import path
from .import views

urlpatterns = [
    path('profile/', views.TeachersProfile, name='teachers-profile'),
    path('register/', views.TeacherRegister, name='teachers-register'),
    path('profile_update/', views.teacher_profile_update, name='tr-profile-update'),
    path('profile_update_trs/<int:student_id>/', views.update_student_info, name='tr-student-profile-update'),
]
