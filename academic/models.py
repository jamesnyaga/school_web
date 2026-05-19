from django.db import models
from school.models import School

class SchoolClass(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=20) 

    def __str__(self):
        return f"{self.school.name} - {self.name}"


class Subject(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Term(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)  

    def __str__(self):
        return self.name


class ExamType(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class StudentMark(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_class = models.ForeignKey('students.Class', on_delete=models.CASCADE)

    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)

    marks = models.IntegerField()
    grade = models.CharField(max_length=2)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'subject', 'term', 'exam_type', 'school')

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.marks}"

class StudentsResults(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)

    total_score = models.FloatField(default=0)
    average_score = models.FloatField(default=0)

    grade = models.CharField(max_length=5, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
