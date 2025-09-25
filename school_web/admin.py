
from django.contrib.admin import AdminSite


class SchoolWebADministration(AdminSite):
    site_header = 'School Web Administration'
    site_title = 'School Web Portal'
    index_title = 'Welcome to Our School Web Admin Area'

admin_site = SchoolWebADministration(name='school_web_admin')