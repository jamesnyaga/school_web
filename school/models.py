from django.db import models
from django.utils import timezone


class School(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # e.g., 'kenya-high' → 'kenyahigh'
        super().save(*args, **kwargs)
    

class GalleryManager(models.Manager):
    def for_school(self, school):
        return self.filter(school=school)


# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    title = models.CharField(max_length=30, default='gallery image', blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    uploaded_at = models.TimeField(default=timezone.now)

    objects = GalleryManager()

    def __str__(self):
        if self.title:
            return f'image {self.title}'
        else:
            return 'Untittled'