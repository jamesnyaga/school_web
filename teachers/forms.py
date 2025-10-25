from django import forms
from .models import Teacher,profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from students.models import User as student_user
from students.models import Assignment, AverageGrade,ClassTeachersComment, resources, Profile,Student,SubjectGrade

#creating the teacher
class TeachersCreationForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#updating the teacher's information by the teacher
class TeachersUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['tr_description']

class TeachersProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']

#updating the student information by the teacher
class Tr_StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email','student_id','full_name','student_class']

class Tr_StudentsUpdateForm(forms.ModelForm):
    class Meta:
        model = student_user
        fields = ['username']

class Tr_StudentAssignmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title','description','due_date']

class Tr_StudentProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class Tr_StudentresourcesUpdateForm(forms.ModelForm):
    class Meta:
        model = resources
        fields = ['title', 'resource_description','resource_file']

class Tr_StudentClassTeachersCommentUpdateForm(forms.ModelForm):
    class Meta:
        model = ClassTeachersComment
        fields = ['student_discipline','comment_on_academics']

class Tr_StudentAverageGradeUpdateForm(forms.ModelForm):
    class Meta:
        model = AverageGrade
        fields = ['Exam_title','date_recorded','grade']

class Tr_StudentSubjectGradeUpdateForm(forms.ModelForm):
    class Meta:
        model = SubjectGrade
        fields = [
            'Exam_title',
            'chemistry_score', 
            'mathematics_score', 
            'physics_score', 
            'biology_score', 
            'history_score', 
            'geography_score', 
            'english_score', 
            'kiswahili_score', 
            'computer_science_score', 
            'art_and_design_score', 
            'music_score', 
            'physical_education_score', 
            'religious_education_score', 
        ]
