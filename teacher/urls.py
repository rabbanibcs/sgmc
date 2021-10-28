from .views import *
from django.urls import path

urlpatterns = [
    path('<int:pk>/',teacher_profile, name='teacher_profile'),
    path('<int:pk>/edit-profile/',teacher_profile_edit,name='teacher_profile_edit'),
]
