from .views import  *
from django.urls import path

urlpatterns = [
   
path("reset-password/",ResetPassword , name="reset_password")
]
