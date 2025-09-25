from django.contrib import admin
from teachers.admin import TeacherAdmin
from .models import (
    Profile, Student, AverageGrade, resources, Assignment,
    SubjectGrade, ClassTeachersComment, Class
)

# Define a custom admin interface for the Student model
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'full_name', 'student_class')
    search_fields = ('student_id', 'full_name')
    list_filter = ('student_class',)

# Define a custom admin interface for the Profile model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('student', 'image')
    search_fields = ('student__student_id',)

# Define admin interfaces for other models as needed
class AverageGradeAdmin(admin.ModelAdmin):
    list_display = ['student','grade','Exam_title']
    search_fields = ('student__student_id', 'grade')

class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date')
    search_fields = ('title',)

class SubjectGradeAdmin(admin.ModelAdmin):
    list_display = ['Exam_title','student']
    search_fields = ['student__student_id']

class ClassTeachersCommentAdmin(admin.ModelAdmin):
    list_display = ('student', 'student_discipline','comment_on_academics')
    search_fields = ('student__student_id',)

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register the models with their respective ModelAdmin classes
admin.site.register(Student, StudentAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AverageGrade, AverageGradeAdmin)
admin.site.register(resources, ResourcesAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(SubjectGrade, SubjectGradeAdmin)
admin.site.register(ClassTeachersComment, ClassTeachersCommentAdmin)
admin.site.register(Class, ClassAdmin)
