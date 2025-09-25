from django import forms
from .models import Gallery
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GalleryUpdateForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image','title','description']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Use forms.EmailField for form fields

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']  # Assign email from form data
        if commit:
            user.save()
        return user