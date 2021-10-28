from django.forms import ModelForm
from .models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['subject', 'designation', 'father',
                  'mother', 'district', 'thana', 'post', 'village',
                  'phone', 'date_of_birth', 'BCS_batch', 'picture','honours','masters','others']




