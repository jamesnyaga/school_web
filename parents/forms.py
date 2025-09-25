from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Parent, Profile
from django.contrib.auth.models import User

class ParentCreationForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=100)
    My_Student_Adm_No = forms.CharField(max_length=10)
    contact = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ParentsUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class ParentUpdateForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['contact']

class ParentProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']