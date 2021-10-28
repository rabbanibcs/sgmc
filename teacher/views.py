from django.contrib import messages
from django.http import HttpResponse,Http404
from teacher.forms import TeacherForm
from django.shortcuts import render, redirect
from user.models import User
from teacher.models import Teacher
# from .tasks import *
from django.contrib.auth.decorators import permission_required,login_required

def teacher_profile(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except Exception as e:
        print(e)
        raise Http404(e)
    teacher=user.get_teacher()
    if teacher:
        context = {
            'teacher': teacher
            }
        return render(request, 'teacher_profile.html', context=context)
    else:
        raise Http404('No Teacher')

        

@login_required
def teacher_profile_edit(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except Exception as e:
        print(e)
        raise Http404(e)

    if pk != request.user.id:
        raise Http404('No student is found')

    teacher=user.get_teacher()
    if request.method == 'POST':
        if teacher:
            form = TeacherForm(request.POST,
                                 request.FILES,
                                 instance=teacher)
        else:
            form = TeacherForm(request.POST, request.FILES)

        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = user
            form.save()
            messages.success(request, 'Your account has been Updated.')
            return redirect('teacher_profile', pk)
    else:
        if teacher:
            form = TeacherForm(instance=teacher)
        else:
            form = TeacherForm()
        # print(form)

    context = {'form': form}
    return render(request, 'teacher_profile_edit.html', context)


