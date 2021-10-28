from django.shortcuts import render
from . models import *
# Create your views here.

def CollectNotice(request,pk):
    notice=NoticeBoard.objects.get(pk=pk)
    return render(request,'notice_board.html',{'notice':notice})
