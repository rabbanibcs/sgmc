from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from college.views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('staff/', include('staff.urls')),
    path('college/', include('college.urls')),
    path('gallery/', include('gallery.urls')),
    path('exam/', include('exam.urls')),
    path('department/', include('department.urls')),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]
# urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
