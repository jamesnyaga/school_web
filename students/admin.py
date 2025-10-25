from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import RelatedOnlyFieldListFilter

from .models import (
    Profile, Student, AverageGrade, resources, Assignment,
    SubjectGrade, ClassTeachersComment, Class
)

# ------------------------------
# Student Model Admin
# ------------------------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'full_name', 'student_class')
    search_fields = ('student_id', 'full_name')
    list_filter = ('student_class',)


# ------------------------------
# Profile Model Admin
# ------------------------------
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('student', 'image')
    search_fields = ('student__student_id',)


# ------------------------------
# AverageGrade Model Admin
# ------------------------------
@admin.register(AverageGrade)
class AverageGradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'grade', 'Exam_title')  # lowercase
    search_fields = ('student__student_id', 'grade')


# ------------------------------
# Resource Model Admin
# ------------------------------
@admin.register(resources)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


# ------------------------------
# Assignment Model Admin
# ------------------------------
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date')
    search_fields = ('title',)


# ------------------------------
# SubjectGrade Model Admin
# ------------------------------
@admin.register(SubjectGrade)
class SubjectGradeAdmin(admin.ModelAdmin):
    list_display = (
        "position_display",
        "student",
        "Exam_title",  #
        "average_score",
        "average_grade_display",
        "teacher_comment_display",  
    )
    list_display_links = ("student",)
    list_filter = (("student__student_class", RelatedOnlyFieldListFilter),)
    search_fields = ("student__full_name", "student__student_id", "Exam_title")

    readonly_fields = (
        "average_score_display",
        "average_grade_display",
    )

    # -----------------------------
    # Average Computation
    # -----------------------------
    def average_score(self, obj):
        scores = [
            obj.chemistry_score, obj.mathematics_score, obj.physics_score,
            obj.biology_score, obj.history_score, obj.geography_score,
            obj.english_score, obj.kiswahili_score, obj.computer_science_score,
            obj.art_and_design_score, obj.music_score,
            obj.physical_education_score, obj.religious_education_score,
        ]
        valid_scores = [s for s in scores if s is not None]
        if not valid_scores:
            return "-"
        return round(sum(valid_scores) / len(valid_scores), 2)
    average_score.short_description = "Average %"

    def average_score_display(self, obj):
        return self.average_score(obj)
    average_score_display.short_description = "Average %"

    def average_grade_display(self, obj):
        avg = self.average_score(obj)
        if avg == "-":
            return "-"
        return obj.get_grade(avg)
    average_grade_display.short_description = "Average Grade"

    # -----------------------------
    # Teacher Comment Display
    # -----------------------------
    def teacher_comment_display(self, obj):
        return obj.teacher_comment if hasattr(obj, "teacher_comment") else "-"
    teacher_comment_display.short_description = "Teacher Comment"

    # -----------------------------
    # Ranking display
    # -----------------------------
    def get_ranked_students(self, obj):
        students = SubjectGrade.objects.filter(
            Exam_title=obj.Exam_title,
            student__student_class=obj.student.student_class
        )
        return sorted(
            students,
            key=lambda s: -sum(filter(None, [
                s.chemistry_score, s.mathematics_score, s.physics_score,
                s.biology_score, s.history_score, s.geography_score,
                s.english_score, s.kiswahili_score, s.computer_science_score,
                s.art_and_design_score, s.music_score,
                s.physical_education_score, s.religious_education_score
            ])) / max(1, len(list(filter(None, [
                s.chemistry_score, s.mathematics_score, s.physics_score,
                s.biology_score, s.history_score, s.geography_score,
                s.english_score, s.kiswahili_score, s.computer_science_score,
                s.art_and_design_score, s.music_score,
                s.physical_education_score, s.religious_education_score
            ]))))
        )

    def position_display(self, obj):
        ranked = self.get_ranked_students(obj)
        position = ranked.index(obj) + 1
        if position == 1:
            emoji, color = "🥇", "#FFD700"
        elif position == 2:
            emoji, color = "🥈", "#C0C0C0"
        elif position == 3:
            emoji, color = "🥉", "#CD7F32"
        else:
            emoji, color = "", "#333"
        return format_html(
            '<span style="font-weight: bold; color: {};">{} {}</span>',
            color, emoji, position
        )
    position_display.short_description = "Position"


# ------------------------------
# ClassTeacherComment Model Admin
# ------------------------------
@admin.register(ClassTeachersComment)
class ClassTeacherCommentAdmin(admin.ModelAdmin):
    list_display = ('student', 'student_discipline', 'comment_on_academics')
    search_fields = ('student__student_id',)


# ------------------------------
# Class Model Admin
# ------------------------------
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
