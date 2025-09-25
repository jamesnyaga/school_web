from django import forms
from .models import BlogPosts

class BlogPostsForm(forms.ModelForm):
	class Meta:
		model = BlogPosts
		fields = ['title','content', 'image','author']