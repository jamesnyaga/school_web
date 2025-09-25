from django.urls import path
from .import views

urlpatterns = [
    path('gallery/', views.gallery_display, name='gallery'),
    path('gallery/add/', views.GalleryUpdate, name='gallery-add'),
]