from django.db import models
from user.models import User
from django.conf import settings
from department.models import Department

designations = (('Lecturer', 'Lecturer'),
                ('Assistant Professor', 'Assistant Professor'),
                ('Associate Professor', 'Associate Professor'),
                ('Professor', 'Professor'))


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    designation = models.CharField(max_length=100, choices=designations, default='lecturer')
    father = models.CharField(max_length=100, null=True, blank=True)
    mother = models.CharField(max_length=100, null=True, blank=True)

    district = models.CharField(max_length=100, null=True, blank=True)
    thana = models.CharField(max_length=100, null=True, blank=True)
    post = models.CharField(max_length=100, null=True, blank=True)
    village = models.CharField(max_length=100, null=True, blank=True)

    picture = models.ImageField(upload_to='pictures/teacher',default='pictures/male.jpeg', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True,
                                     help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    phone = models.IntegerField(null=True, blank=True)
    BCS_batch = models.IntegerField(null=True, blank=True)
    honours=models.CharField(max_length=200,default='',blank=True)
    masters=models.CharField(max_length=200,default='',blank=True)
    others=models.CharField(max_length=200,default='',blank=True)

    def __str__(self):
        return self.user.name.upper()