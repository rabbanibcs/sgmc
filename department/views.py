from django.shortcuts import render
from gallery.models import *
from exam.models import Examination
from department.models import Department
from teacher.models import Teacher


def department(request,pk):
    try:
        exams= Examination.objects.all()
    except:
        exams=None 
    subject = Department.objects.get(pk=pk)
    teachers = Teacher.objects.filter(subject=subject)
    notices=NoticeBoard.objects.filter(department=subject).order_by('-created_on')
    # print(notices)

    context = {'teachers': teachers,'subject':subject,'exams':exams,'notices':notices}
    return render(request, 'department.html', context)

