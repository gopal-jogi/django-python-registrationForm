from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def registration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}

    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST, request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            MUFDO=UFD.save(commit=False)
            pw=UFD.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO=PFD.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('Register successfully',
                      '''Hello
                        
                        Thank you you Register successfully''',
                        'gopaljogi420@gmail.com',
                        [MUFDO.email],
                        fail_silently=False)
            return HttpResponse("Registration Successfully")
        else:
            return HttpResponse("Invalide data")
    return render(request,'registration.html',d)