from django.db import models
from django.conf import settings

group = (('SC','Science'),('HM','Humanities'),('BS','Business studies'))


class Department(models.Model):
    name = models.CharField(max_length=100,unique=True)
    subject = models.CharField(max_length=100)
    group = models.CharField(choices=group,max_length=20)

    def __str__(self):
        return self.name

    def get_subjectCode(self):

        return SubjectCode.objects.get(subject_name__icontains=self.subject)


choices = (('CS', 'Compulsory'), ('SC ', 'Science '), \
           ('BS', 'Business Studies'), ('HM ', 'Humanities'))


class SubjectCode(models.Model):
    subject_name = models.CharField(max_length=100)
    code = models.CharField(max_length=7)
    type = models.CharField(choices=choices, default='CS', max_length=100)

    def __str__(self):
        return self.subject_name