from . import views
from django.urls import path

urlpatterns = [
    path('upload/',views.upload_file,name='upload_studentInfo'),
    path('<int:pk>/',views.student_profile, name='student_profile'),
    path('list/',views.students_list, name='students_list'),
    path('<int:pk>/edit-profile/', views.student_profile_edit, name='student_profile_edit'),
]
