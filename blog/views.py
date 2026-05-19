from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import BlogPosts
from school.models import School, Gallery


# =========================
# HELPER FUNCTION
# =========================
def get_current_school(school_slug):
    """
    Returns the correct school based on slug.
    Falls back to EDU001 if slug is not provided.
    """
    if school_slug:
        return get_object_or_404(School, slug=school_slug.lower())

    return get_object_or_404(School, code='EDU001')


# =========================
# BLOG LIST VIEW
# =========================
def Post_list(request, school_slug=None):
    school = get_current_school(school_slug)

    posts = BlogPosts.objects.filter(
        school=school
    ).order_by('-date_posted')

    return render(request, 'blog/blog_posts.html', {
        'posts': posts,
        'school': school,
        'school_slug':school_slug
    })


# =========================
# BLOG DETAIL VIEW
# =========================
def PostDetails(request, id, school_slug=None):
    school = get_current_school(school_slug)

    post = get_object_or_404(
        BlogPosts,
        id=id,
        school=school
    )

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'school': school,
        'school_slug':school_slug
    })

def latestPosts(request, school_slug=None):
    school = get_current_school(school_slug)

    posts = BlogPosts.objects.all().order_by('-created_at')

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'school': school,
        'school_slug':school_slug
    })
# =========================
# HOME VIEW
# =========================
def home(request, school_slug=None):
    school = get_current_school(school_slug)

    gallery_images = Gallery.objects.filter(
        school=school
    )

    posts = BlogPosts.objects.filter(
        school=school
    ).order_by('-date_posted')

    return render(request, 'blog/home.html', {
        'school': school,
        'gallery_images': gallery_images,
        'posts': posts,
    })


# =========================
# GALLERY VIEW (FIXED)
# SAME FUNCTIONALITY AS BLOG
# =========================
def gallery_display(request, school_slug=None):

    school = get_object_or_404(School, slug=school_slug)

    images = Gallery.objects.filter(school=school)

    return render(request, 'school/gallery.html', {
        'images': images,
        'school': school
    })


# =========================
# STATIC PAGES (SCHOOL BASED)
# =========================
def about(request, school_slug=None):
    school = get_current_school(school_slug)

    return render(request, 'blog/about.html', {'school': school,'school_slug':school_slug})


def Academics(request, school_slug=None):
    school = get_current_school(school_slug)

    return render(request, 'blog/academics.html', {'school': school})


def Admission(request, school_slug=None):
    school = get_current_school(school_slug)

    return render(request, 'blog/admission.html', {'school': school})


def Student_lifes(request, school_slug=None):
    school = get_current_school(school_slug)

    return render(request, 'blog/student_lifes.html', {'school': school})


def login(request, school_slug=None):
    school = get_current_school(school_slug)

    # SAFETY CHECK (critical)
    if not school.slug:
        school.slug = school.code.lower()

    return render(request, 'blog/login.html', {
        'school': school
    })


def announcements(request, school_slug):
    school = get_current_school(school_slug)

    return render(request, 'blog/announcements.html', {'school': school})


def calendars(request, school_slug=None):
    school = get_current_school(school_slug)

    return render(request, 'blog/calendars.html', {'school': school})


def Others(request, school_slug=None):
    school = get_current_school(school_slug)

    return render(request, 'blog/others.html', {'school': school})