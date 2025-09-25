from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from students.models import User as user
from .models import Student, Profile, Class

class StudentRegistration(UserCreationForm):
    student_id = forms.CharField(max_length=10)
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    student_class = forms.ModelChoiceField(queryset=Class.objects.all(), help_text='Please select your class')
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2025)))

    class Meta:
        model = User
        fields = ['username', 'email', 'student_id', 'full_name', 'date_of_birth', 'password1', 'password2', 'student_class']

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if Student.objects.filter(student_id=student_id).exists():
            raise forms.ValidationError('A Student with that Id already exists.')
        return student_id


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            student = Student.objects.create(
                user=user,
                student_id=self.cleaned_data['student_id'],
                username=user.username,  # Assuming username in Student is same as User's username
                full_name=self.cleaned_data['full_name'],
                student_class=self.cleaned_data['student_class'],
                date_of_birth=self.cleaned_data['date_of_birth']
            )
            student.save()
        return user
class StudentsUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username','email']

class StudentsProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']