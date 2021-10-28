from django.contrib import admin
from import_export.admin import ImportMixin

from .models import *
from import_export.resources import ModelResource
from .models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'section',
        'class_roll',
        'group',
        'phone',
        'optional_subjects',
        
    )
    list_filter = ('class_roll', 'date_of_birth')
    search_fields = ('group', 'class_roll')



@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'group', 'admission_year', 'active')
    list_filter = ('active',)
