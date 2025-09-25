from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class BlogPosts(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	image = models.ImageField(upload_to = 'blog_images/',blank=True, null=True)
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)


	def __str__(self):
		return self.title
