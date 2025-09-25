from django.contrib import admin
from .models import Parent, Profile
# Register your models here.

class ParentsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'My_Student_Adm_No')
    search_fields = ('my_student__student_id',)
admin.site.register(Parent, ParentsAdmin)
admin.site.register(Profile)