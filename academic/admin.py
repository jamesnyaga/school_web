from django.contrib import admin
from .models import SchoolClass, Subject, Term, ExamType, StudentMark,StudentsResults


admin.site.register(SchoolClass)
admin.site.register(Subject)
admin.site.register(Term)
admin.site.register(ExamType)
admin.site.register(StudentMark)
admin.site.register(StudentsResults)