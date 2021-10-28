from django.urls import path
from .views import marks_input,student_result,all_students_result


urlpatterns = [
    # marks/
    # path('<str:sub>/<str:term>/<int:year>/<int:roll>/',marks_input,name='marks-input'),
    path('<str:sub>/<str:term>/<int:year>/', marks_input, name='marks'),
    path('<str:session>/<int:roll>/<str:year>/<str:term>/',student_result,name='student_result'),
    path('<str:sub>/<int:year>/<str:term>/',all_students_result, name='all_students_result'),
]