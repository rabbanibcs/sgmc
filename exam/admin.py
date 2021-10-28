from django.contrib import admin
from .models import Examination,Grade

@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'term','session','is_active', 'is_published')
    list_filter = ('year', 'term')
    list_display_links = ('term', 'id')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'examination',
        'session',
        'subject',
        'roll',
        'total_marks',
        'grade',
        'point',
    )
    list_filter = ('examination', 'session','roll','subject')
    search_fields = ( 'roll',)
    list_display_links = ('examination', )
    save_on_top = True


