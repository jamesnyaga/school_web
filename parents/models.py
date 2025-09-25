from django.db import models
from django.contrib.auth.models import User
from students.models import Student

# Create your models here.
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='parent')
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, default=None)
    contact = models.CharField(max_length=10)
    My_Student_Adm_No = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.full_name} parent of {self.My_Student_Adm_No.full_name}"


class Profile(models.Model):
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    image = models.ImageField(default='parents_default_img.jpeg', upload_to='parents_profiles')

    def __str__(self):
        return f"{self.parent} profile"