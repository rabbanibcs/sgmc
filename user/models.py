from django.db import models
from django.contrib.auth.models import AbstractUser
# from student.models import Student
# from teacher.models import Teacher
from .managers import CustomUserManager


class User(AbstractUser):
    first_name = None
    last_name = None
    username = None
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    gender=models.CharField(max_length=1, default='F')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)  # is not a teacher
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]
    objects = CustomUserManager()

    def get_full_name(self):
        return self.name
    # @property
    # def first_name(self):
    #     a = self.name.split(' ')
    #     return a[0]

    def __str__(self):
        return self.name.upper()

    def get_student(self):
        try:
            # student = Student.objects.get(user=self)
            student = self.student
            print(student)
        except:
            return False
        return student

    def get_teacher(self):
        try:
            teacher = self.teacher
            # print(teacher)
        except:
            return False
        return teacher


