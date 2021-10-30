from django.urls import path
from .views import *


urlpatterns = [
    # marks/
    path('each/', marks_of_each_sub, name='each_sub_marks'),
    path('<str:sub>/<str:term>/<int:year>/', marks_input, name='marks'),
    path('<str:session>/<int:roll>/<str:year>/<str:term>/',student_result,name='student_result'),
    path('<str:sub>/<int:year>/<str:term>/',all_students_result, name='all_students_result'),
]