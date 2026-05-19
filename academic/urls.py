from django.urls import path
from . import views

urlpatterns = [
    path('academic/marks-entry/', views.marks_entry, name='marks-entry'),
    path("ajax/save-mark/", views.ajax_save_mark, name="save_mark_ajax"),
    ]