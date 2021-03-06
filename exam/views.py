from exam.forms import ExamCreation
from django.shortcuts import render, redirect
from .forms import MarksForm, MarksFormScience
from student.models import Student
from .models import Grade, Examination
from department.models import Department,SubjectCode
from django.http import HttpResponse, JsonResponse
from .tasks import *
from django.contrib.auth.decorators import permission_required,login_required

# @permission_required('exam.add_grade',raise_exception=True)
@login_required
def marks_input(request, sub, term, year):
    # students are not allowed
    if not request.user.is_teacher :
        message='You are not allowed to do this.'
        return render(request, 'not-allowed.html',{'message':message})

    # teachers from other department  are not allowed

    if sub != str(request.user.teacher.subject):
        # print('not a teacher of this department')
        message='You are not a teacher of this department'
        return render(request, 'not-allowed.html',{'message':message})

    roll=request.POST.get('roll')
    examination = Examination.objects.get(year=year, term=term)
    # print(examination.session,'examination.session')
    department = Department.objects.get(name__icontains=sub)
    subject_code=department.get_subjectCode()
    subCode=subject_code.code
    subCode=subCode.split(',')
    print('sub_code',subCode)
    if roll:
        students= Student.objects.filter(session=examination.session,class_roll__gte=roll,subjects__icontains=subCode[0]).order_by('class_roll')
        # print('total students in database: ',students.count())
    else:
        students= Student.objects.filter(session=examination.session,subjects__icontains=subCode[0]).order_by('class_roll')
        # print('total students in database: ',students.count())

    # print(students[0].subjects)
    student=students[0]
    # print(student.session,'session')
    # print(student.user.name,'name')

    grade = get_grade_object(examination,department,student)
    # print('grade_ object: ', grade)




    entries_done=Grade.objects.filter(examination=examination.id,subject=department).values('roll').order_by('roll')
    context = {'grade':grade,
    'examination': examination, 
    'student': student,
     'department': department,
     'entries_done':entries_done,
     }
    
    # print(entries_done)
    if request.method == 'POST':
        if department.group == 'SC':
            form = MarksFormScience(request.POST)
        else:
            form = MarksForm(request.POST)
        if form.is_valid():
            save_form_data(request,examination,department,grade,student)

            if students.count()==1:
                message='You have done a great Job.'
                return render(request, 'congrates.html',{'message': message})


            student=students[1]
            # print(student.class_roll)
            grade = get_grade_object(examination,department,student)
            context = {'grade':grade,
            'examination': examination,
             'student': student, 
             'department': department,
             'entries_done':entries_done,
             }
            return render(request, 'marks_input.html', context)
        else:
            context = {'form':form,
            'grade':grade,
            'examination': examination, 
            'student': student, 
            'department': department,
            'entries_done':entries_done,
            }
            return render(request, 'marks_input.html', context)
    else:
        return render(request, 'marks_input.html', context)

@login_required
def student_result(request, session, roll, year, term):
    
    # logedin student con not look at other's result
    if not request.user.is_teacher and request.user.student.class_roll  != roll :
        message='You are not allowed to look at your friend\'s result.'
        return render(request, 'not-allowed.html',{'message':message})
    if not request.user.is_teacher and request.user.student.session != session :
        message='You are not allowed to look at other\'s result.'
        return render(request, 'not-allowed.html',{'message':message})

    exam = get_exam(year, term, session)
    try:
        student = Student.objects.get(class_roll=roll,session=session)

    except Exception as e:
        print(e)
        return render(request, 'not-allowed.html',{'message':e})

    results = Grade.objects.filter(roll=roll,session=session, examination=exam)
    return render(request, 'student_result.html', {'results': results, 'exam': exam, 'student': student})

from django.core.paginator import Paginator
@login_required
def all_students_result(request,sub, year, term):
    page_num=request.GET.get('page',1)
    exam = get_exam(year,term)
    # print(exam)
    subject = Department.objects.get(name=sub)
    # print(subject.group)
    results = Grade.objects.filter(examination=exam,subject=subject).order_by('roll')
    
    p = Paginator(results, 5)
    page=p.page(page_num)

    # result = Grade.objects.all()
    # print(results)
    return render(request, 'all_students_result.html', 
    {'page_obj': page,
     'exam': exam,
     'subject':subject,
     'session':exam.session})

from django.core import serializers

def marks_of_each_sub(request):
    roll=request.GET.get('roll')
    exam_id=request.GET.get('exam_id')
    subject=request.GET.get('subject')
    exam=Examination.objects.get(pk=exam_id)
    subject = Department.objects.get(subject__icontains=subject)
    try:
        grade=Grade.objects.get(examination=exam,roll=roll,subject=subject)
        data=grade.get_dict()
        # print(data)
        # data = serializers.serialize("json", [data],fields=('cq_marks','mcq_marks','practical_marks'))
        # return HttpResponse(data, content_type='application/json')
    except Exception as e:
        data={'error':'Object does not exists.'}

    return JsonResponse(data)

    