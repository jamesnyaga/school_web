from school.models import School

def school_context(request):
    school = School.objects.filter(code='EDU001').first()
    return {'school': school}