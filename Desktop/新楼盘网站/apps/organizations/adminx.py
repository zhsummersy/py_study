import xadmin

from apps.organizations.models import Teacher, CourseOrg, City


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']


class CourseOrgAdmin(object):
    list_display = ['name', "add_time"]
    search_fields = ['name', "add_time"]
    list_filter = ['name', "add_time"]
    style_fields = {
        "desc": "ueditor"
    }


class CityAdmin(object):
    list_display = ["id", "name", "desc"]
    search_fields = ["name", "desc"]
    list_filter = ["name", "desc", "add_time"]
    list_editable = ["name", "desc"]


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(City, CityAdmin)
