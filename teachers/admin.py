from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Teacher, profile
from students.models import Student

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name','class_teacher','student_count_link')

    def student_count_link(self, teacher):
        count =  Student.objects.filter(student_class=teacher.class_teacher).count()
        students = Student.objects.filter(student_class=teacher.class_teacher)
        url = (
            reverse(
                "admin:students_student_changelist")
                +f"?class_teacher_id_exact={teacher.class_teacher}"
        )
        return format_html('<a href="{}">{} students</a>', url, count)
    student_count_link.short_description = 'number of students'
# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(profile)