from django.db import models
from django.utils import timezone

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    title = models.CharField(max_length=30, default='gallery image', blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    uploaded_at = models.TimeField(default=timezone.now)

    def __str__(self):
        if self.title:
            return f'image {self.title}'
        else:
            return 'Untittled'
