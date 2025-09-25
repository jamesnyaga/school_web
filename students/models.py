from django.db import models, transaction
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Class(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
	student_id = models.CharField(max_length=10, unique=True)
	username = models.CharField(max_length=30, unique=True, default='student')
	email = models.EmailField(blank=True)
	student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
	full_name = models.CharField(max_length=100)
	date_of_birth = models.DateField()


	def __str__(self):
		return f'{self.full_name} ({self.student_id}) in {self.student_class}'
	
	def save(self, *args, **kwargs):
		if not self.email:
			self.email = f'student{self.student_id}@gamail.com'
		with transaction.atomic():
			super().save(*args, **kwargs)
			if self.user.email != self.email:
				self.user.email = self.email
				self.user.save(update_fields=['email'])
				
class AverageGrade(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='average_grades')
	Exam_title = models.CharField(max_length=50)
	grade = models.CharField(max_length=2)
	date_recorded = models.DateField()

	def __str__(self):
		return f"{self.student.student_id}: {self.grade}" 

class Assignment(models.Model):
	student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='assignments')
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	due_date = models.DateField()

	def __str__(self):
		return self.title 

class ClassTeachersComment(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='comments')
	student_discipline = models.TextField()
	comment_on_academics = models.TextField()

	def __str__(self):
		return f"class teacher's comments about {self.student}"

class resources(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='resources',default=None)
	title = models.CharField(max_length = 100)
	resource_description = models.TextField(default=None)
	resource_file = models.FileField(upload_to='student/resources')

	def __str__(self):
		return self.title
	
class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    image = models.ImageField(default='student_default_img.jpg',upload_to='student_profiles')

    def __str__(self):
        return f'{self.student.student_id} profile'
	
    """def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height >300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)"""


			


class SubjectGrade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subject_grades')
    Exam_title = models.CharField(max_length=50, default='Kianyaga boys form 4 exam')
    chemistry_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    chemistry_grade = models.CharField(max_length=2, blank=True, null=True)
    mathematics_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    mathematics_grade = models.CharField(max_length=2, blank=True, null=True)
    physics_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    physics_grade = models.CharField(max_length=2, blank=True, null=True)
    biology_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    biology_grade = models.CharField(max_length=2, blank=True, null=True)
    history_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    history_grade = models.CharField(max_length=2, blank=True, null=True)
    geography_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    geography_grade = models.CharField(max_length=2, blank=True, null=True)
    english_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    english_grade = models.CharField(max_length=2, blank=True, null=True)
    kiswahili_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    kiswahili_grade = models.CharField(max_length=2, blank=True, null=True)
    computer_science_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    computer_science_grade = models.CharField(max_length=2, blank=True, null=True)
    art_and_design_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    art_and_design_grade = models.CharField(max_length=2, blank=True, null=True)
    music_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    music_grade = models.CharField(max_length=2, blank=True, null=True)
    physical_education_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    physical_education_grade = models.CharField(max_length=2, blank=True, null=True)
    religious_education_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    religious_education_grade = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"Grades for {self.student} in {self.Exam_title}"