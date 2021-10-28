from django.contrib import admin
from teacher.models import Teacher

# admin.site.register(Teacher)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'subject',
        'designation',
        'date_of_birth',
        'phone',
        'BCS_batch',
    )
    list_filter = ('user', 'subject', 'date_of_birth')