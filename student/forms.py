from django.forms import ModelForm
from django import forms
from .models import *


class UploadFileForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file','group','admission_year']


class StudentProfileForm(ModelForm):
    name= forms.CharField(max_length=150,required=False,initial="Your Name...")
    class Meta:
        model = Student
        fields = ['name','father_name','mother_name','district','thana','post','village','picture','date_of_birth','phone']




