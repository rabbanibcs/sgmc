from django.shortcuts import render
from exam.forms import ExamCreation
from department.models import Department
from teacher.models import Teacher
from exam.models import Examination
from gallery.models import Event, Carousel
from gallery.models import *


def home(request):
    events = Event.objects.order_by('-published_date')[:3]
    notices=NoticeBoard.objects.all().order_by('-created_on')
    return render(request, 'home.html',{'events':events,'notices':notices})



