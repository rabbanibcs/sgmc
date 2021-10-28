from user.models import User
from student.models import Student
from department.models import SubjectCode
from time import sleep
from student.models import FileUpload
import pandas as pd
import threading
import concurrent.futures
from .forms import *
from django.http import HttpResponse
from exam.models import Examination


def handle_uploaded_file(f,group,admission_year):
    group=group
    file = FileUpload.objects.get(active=False)
    file.active = True
    file.save()
    df = pd.read_excel(file.file,nrows=50)
    columns=list(df.columns)
    columns.sort()
    expected_columns=['Section Roll', 'Subjects', 'Optional','Gender']
    expected_columns.sort()
    print('columns',columns)
    print('expected_columns',expected_columns)
    for column in columns:
        if column in expected_columns:
            print('match',column)
        else:
            print('no match',column)
            return False

    tasks=[]
    for i in range(len(df)):
        optional_subjects = df.iloc[i]['Optional']
        optional_subjects = str(optional_subjects).replace('\n', ',')
        # print('optional_subjects',optional_subjects)
        Section_Roll = str(df.iloc[i]['Section Roll']).replace(' ', ',').replace('\n',',').split(',')
        # print('Section_Roll',Section_Roll)
        class_roll=Section_Roll[1]
        subjects = str(df.iloc[i]['Subjects']).replace(' ','').replace('\n', '')
        gender = df.iloc[i]['Gender']
        # print('subjects',subjects)
        # PassYear_RollNo_Board_RegNo = df.iloc[i]['PassYear Roll No Board RegNo'].replace('\n', ' ')
        # PassYear_RollNo_Board_RegNo = PassYear_RollNo_Board_RegNo.split(' ')
        # print('PassYear_RollNo_Board_RegNo',PassYear_RollNo_Board_RegNo)
        
        t=threading.Thread(target=create_student_user, args=[group,admission_year,gender,Section_Roll,optional_subjects,subjects])
        t.start()
        tasks.append(t)
    for task in tasks:
        task.join()
    
    return True



def create_student_user(group,admission_year,gender,Section_Roll,optional_subjects,subjects):
    email = f'{admission_year}-{Section_Roll[1]}@sgmc.com'
    password = f'{Section_Roll[1]}{Section_Roll[1]}'
    name =f'{admission_year}-{Section_Roll[1]}'

    try:
        user=User.objects.get(email=email)
        print(f'account exists for {user.email}')
    except:
        user = User.objects.create_user(name=name, email=email, password=password)
        print(f'account creating for {user.email}')
    create_student_profile(user,group,admission_year,gender,Section_Roll,optional_subjects,subjects)
    return user


def create_student_profile(user,group,admission_year,gender,Section_Roll,optional_subjects,subjects):
    admission_year=int(admission_year)
    student=Student.objects.get_or_create(
        user=user,
        group=group,
        admission_year=admission_year,
        section=Section_Roll[0],
        class_roll= Section_Roll[1],
        optional_subjects=optional_subjects,
        subjects=subjects,
        session=f'{admission_year}-{admission_year+1}'

    )
    
    return student


def get_profile_form(data=None, files=None, instance=None):
    form = StudentProfileForm(data=data, files=files, instance=instance)
    return form

def get_exams():
    try:
        exams = Examination.objects.all()
        # print(exams)
    except:
        return False
    return exams











