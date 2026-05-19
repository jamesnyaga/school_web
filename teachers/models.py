from django.db import models
from django.contrib.auth.models import User
from academic.models import SchoolClass
from school.models import School


# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=30, unique=False)
    tr_description = models.TextField()
    class_teacher = models.ForeignKey(SchoolClass, on_delete=models.SET_NULL, null=True, blank=True)
    
    def my_students(self):
        return Student.objects.for_school(self.school).filter(student_class=self.class_teacher)
        
    def __str__(self):
        return f'Teacher {self.full_name} profile({self.class_teacher})'

class profile(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    image = models.ImageField(default='tr_default_profile.jpeg', upload_to='teachers_profile')

    def __str__(self):
        return f'Profile for {self.teacher.full_name}'




