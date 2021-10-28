from django.db import models
from django.conf import settings
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from department.models import SubjectCode


def current_year():
    return datetime.date.today().year
current_year=current_year()


def max_value_current_year(value):
    return MaxValueValidator(current_year+1)

group = (('science', 'Science'), ('humanities', 'Humanities'), ('business studies', 'Business Studies'))
com_sub = (('Bengali', 'Bengali'), ('English', 'English'), ('ICT', 'ICT'))
session=[(f'{s}-{s+1}',f'{s}-{s+1}') for s in range(2015,2051)]


class FileUpload(models.Model):
    file = models.FileField(upload_to='files')
    group = models.CharField(choices=group, default='science', max_length=20)
    admission_year=models.PositiveIntegerField( 
        default=current_year, 
        validators=[MinValueValidator(2015),
         max_value_current_year])
    active = models.BooleanField(default=False)


class Student(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100, default='', blank=True)
    mother_name = models.CharField(max_length=100, default='', blank=True)
    section = models.CharField(max_length=20,default='A')
    class_roll = models.PositiveIntegerField()
    group = models.CharField(choices=group, default='science', max_length=20)
    district = models.CharField(max_length=100, default='', blank=True)
    thana = models.CharField(max_length=100, default='', blank=True)
    post = models.CharField(max_length=100, default='', blank=True)
    village = models.CharField(max_length=100, default='', blank=True)

    picture = models.ImageField(upload_to='student',default='pictures/girl.png', blank=True)
    date_of_birth = models.DateField(default='2000-12-01', blank=True,
                                     help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    phone = models.CharField(default='', blank=True,max_length=11)
    optional_subjects = models.CharField(max_length=100,default='')
    subjects = models.CharField(max_length=200,default='')
    #ssc info

    ssc_pass_year = models.CharField(max_length=4,default='')
    ssc_roll = models.CharField(max_length=6,default='')
    board = models.CharField(max_length=50,default='MYMENSINGH')
    registration_no = models.CharField(max_length=100,default='')
    #hsc info
    session = models.CharField(choices=session,max_length=9,default=f'{current_year}-{current_year+1}')
    regular=models.BooleanField(default=True)
    admission_year=models.PositiveIntegerField( 
        default=current_year, 
        validators=[MinValueValidator(2020),
         max_value_current_year])

    def __str__(self):
        return str(self.class_roll)


    # get compusory subjects
    def get_compulsory_subjects(self):
        subject_codes=self.subjects.split(',')
        # print(subject_codes)
        subjects=set()
        for subject_code in subject_codes:
            subject=SubjectCode.objects.get(code__contains=subject_code)
            subjects.add(subject.subject_name)
        return subjects

    # get optional subjects
    def get_optional_subject(self):
        optional_subject_codes=self.optional_subjects.split(',')
        optional_subjects=set()
        for optional_subject_code in optional_subject_codes:
            optional_subject=SubjectCode.objects.get(code__contains=optional_subject_code)
            optional_subjects.add(optional_subject.subject_name)
        return optional_subjects

    def sudent_has_this_subject(self,subCode):
        subjects = self.subjects.split(',')
        # subjects = subjects
        # print(subjects)
        for subject in subjects:
            if subject==subCode[0]:
                # print(subject,subCode[0])
                return True
        return False
        
