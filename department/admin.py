from django.contrib import admin
from department.models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'group')
    search_fields = ('name',)
    list_display_links = ( 'name',)

@admin.register(SubjectCode)
class SubjectCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_name', 'code', 'type')
    search_fields = ('subject_name',)
    list_display_links = ( 'subject_name',)


# # @admin.register(SubjectCode)
# class SubjectCodeAdmin(admin.TabularInline):
#     model = SubjectCode

# # admin.site.register(SubjectCodeAdmin)
