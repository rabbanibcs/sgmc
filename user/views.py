from django.shortcuts import render, redirect
from .forms import *
from user.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required,login_required

@login_required
def ResetPassword(request):
    if request.method=='POST':
        form= PasswordResetForm(request.POST)
        print(form)
        user=request.user
        if form.is_valid():

            if request.POST.get('new_password')==request.POST.get('new_password_again'):
                user.set_password(request.POST.get('new_password'))
                user.save()
                login(request, user)
                return redirect('home')
            else:
                error='Passwords didn\'t match '
                return render(request,'password-reset.html',{'form':form,'error':error})
            
        else:
            return render(request,'password-reset.html',{'form':form})

    else:
        form= PasswordResetForm()
        # print(form)
        return render(request,'password-reset.html',{'form':form})



