from django.contrib import admin
from .models import *

# admin.site.register(Gallery)
# admin.site.register(Carousel)
# admin.site.register(NoticeBoard)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'published_date',
    )
    list_filter = ('published_date', 'title',)
    list_display_links = ('title', )


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title', )
    list_filter = ('title',)


@admin.register(NoticeBoard)
class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'created_on', 'department')
    list_filter = ('created_on', 'department')
    list_display_links = ('title', )
