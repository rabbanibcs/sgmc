from django.contrib import messages
from django.shortcuts import render, redirect
# from .helpers import *
from student.models import *
from user.models import User
from .forms import *
from django.http import HttpResponse,Http404
from exam.models import Examination
from .tasks import *
import time
from django.contrib.auth.decorators import permission_required,login_required


@permission_required('student.add_file_upload',raise_exception=True)
def upload_file(request):
    if request.method == 'POST':
        start_time=time.time()
        admission_year=request.POST.get('admission_year')
        group=request.POST.get('group')
        form = UploadFileForm(request.POST, request.FILES)
        # print(request.FILES.get('file'))
        file_name=str(request.FILES.get('file'))
        file_extension=file_name.split('.')[-1]
        # print(file_extension)
        if file_extension != 'xlsx':
            message='This is not a XLSX file'
            return render(request, 'upload.html', {'form': form,'message':message})
        for a,b in request.FILES.items():
            print(a,b)
        if form.is_valid():
            form.save()
            result=handle_uploaded_file(request.FILES['file'],group,admission_year)
            if not result:
                message='Sorry. Plz check column names in your file '
                return render(request, 'upload.html', {'form': form,'message':message})


            duration=time.time()-start_time
            # print(duration)
            return HttpResponse('success '+str(duration)+' s')
        else:
            return render(request, 'upload.html', {'form': form})

    else:
        form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})


@login_required
def student_profile(request, pk):
    exams = get_exams()
    try:
        user = User.objects.get(pk=pk)
    except Exception as e:
        print(e)
        raise Http404(e)

    student = user.get_student()
    if not student:
        raise Http404('No student is found')
    else:
        subjects=student.get_compulsory_subjects()
        optional_subjects=student.get_optional_subject()
        compulsory_subjects=subjects.difference(optional_subjects)
        context = {
            'student': student,
            'compulsory_subjects':compulsory_subjects,
            'optional_subject':optional_subjects,
            'exams': exams}
        return render(request, 'student_profile.html', context)

@login_required
def student_profile_edit(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except Exception as e:
        # print(e)
        raise Http404(e)
        
    # logedin student can not edit other's profile
    if pk != request.user.id:
        raise Http404('No student is found')

    student = user.get_student()
    if request.method == 'POST':
        if student:
            form = get_profile_form(data=request.POST, files=request.FILES, instance=student)
        else:
            form = get_profile_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = user
            user.name=request.POST.get('name')
            user.save()
            form.save()
            messages.success(request, 'Your account has been Updated.')
            return redirect('student_profile', pk)
    else:
        if student:
            form = get_profile_form(instance=student)
        else:
            form = get_profile_form()
    context = {'form': form, 'student': student}
    return render(request, 'student_profile_edit.html', context)



@login_required
def students_list(request):
    page=request.GET.get('page',1)
    session=request.GET.get('session')
    total_items=int(page)*25
    sessions=Student.objects.all().values('session').distinct()[0:3]
    # print('session',session)
    initial=total_items-25
    group=request.GET.get('group')
    
    data={'group':group,'page':page,'loaded':total_items,'sessions':sessions,'session':session}
    # print(data)
    students = Student.objects.filter(group=group,session=session).order_by('class_roll')
    total_students=len(students)
    students=students[initial:total_items]
    return render(request, 'students_list.html',{'students':students,'data':data,'total':total_students})

