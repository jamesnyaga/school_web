from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from school.models import School
import json

from .models import StudentMark, Subject, Term, ExamType, StudentsResults
from students.models import Student
from students.models import Class


def calculate_grade(marks):
    marks = int(marks)

    if marks >= 80:
        return "A"
    elif marks >= 75:
        return "A-"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 56:
        return "B-"
    elif marks >= 55:
        return "C+"
    elif marks >= 50:
        return "C"
    elif marks >= 45:
        return "C-"
    elif marks >= 40:
        return "D+"
    elif marks >= 35:
        return "D"
    elif marks >= 30:
        return "D-"
    else:
        return "E"


def marks_entry(request, school_slug):
    school = get_object_or_404(School, slug=school_slug)
    classes = Class.objects.filter(school=school)
    subjects = Subject.objects.all()
    terms = Term.objects.all()
    exams = ExamType.objects.all()

    context = {
        "classes": classes,
        "subjects": subjects,
        "terms": terms,
        "exams": exams,
        "school": school,
    }

    class_id = request.GET.get("class")
    subject_id = request.GET.get("subject")
    term_id = request.GET.get("term")
    exam_id = request.GET.get("exam")

    if class_id and subject_id and term_id and exam_id:

        students = Student.objects.filter(student_class_id=class_id)

        marks = StudentMark.objects.filter(
            student__in=students,
            subject_id=subject_id,
            term_id=term_id,
            exam_type_id=exam_id
        )

        # build dictionary
        marks_map = {}
        for mark in marks:
            marks_map[mark.student_id] = mark.marks

        # attach marks to each student
        for student in students:
            student.saved_marks = marks_map.get(student.id, "")

        context.update({
            "students": students,
            "selected_class": int(class_id),
            "selected_subject": int(subject_id),
            "selected_term": int(term_id),
            "selected_exam": int(exam_id),
        })

    return render(request, "academic/marks_entry.html", context)





def update_students_results(student, term, exam_type):
    term = student.objects.get(id=term_id)
    exam_type = student.objects.get(id=exam_id)

    marks = StudentMark.objects.filter(
        student=student,
        term=term,
        exam_type=exam_type
    )

    print("MARKS FOUND:", marks.count())

    total = sum(m.marks for m in marks)
    count = marks.count()

    avg = total / count if count > 0 else 0
    grade = calculate_grade(avg)

    StudentsResults.objects.update_or_create(
        student=student,
        term=term,
        exam_type=exam_type,
        defaults={
            "total_score": total,
            "average_score": avg,
            "grade": grade
        }
    )
    update_students_results(student, term, exam_type)

@csrf_exempt
def ajax_save_mark(request, school_slug):
    if request.method == "POST":
        data = json.loads(request.body)

        student_id = data.get("student_id")
        marks = data.get("marks")
        subject_id = data.get("subject_id")
        term_id = data.get("term_id")
        exam_id = data.get("exam_id")

        if marks == "" or marks is None:
            return JsonResponse({"success": False})

        marks = int(marks)

        if marks > 100:
            return JsonResponse({"success": False})

        grade = calculate_grade(marks)

        student = Student.objects.get(id=student_id)
        school = student.school
        school_class = student.student_class 
        
        # if it's NOT a model instance, convert it
        if not isinstance(school_class, Class):
            school_class = Class.objects.get(name=school_class)

        StudentMark.objects.update_or_create(
            student_id=student_id,
            subject_id=subject_id,
            term_id=term_id,
            exam_type_id=exam_id,
            defaults={
                "marks": marks,
                "grade": grade,
                "school": student.school,
                "school_class": student.student_class 
            }
        )

        return JsonResponse({
            "success": True,
            "grade": grade
        })
