from django.urls import path

from department.views import department

urlpatterns = [
    path('<int:pk>/', department, name='department'),

]