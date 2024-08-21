from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def create_studentform(request):
    STFO=Student_Form()
    d={'STFO':STFO}
    if request.method=='POST':
          STDO=Student_Form(request.POST)
          if STDO.is_valid():
                Sn=STDO.cleaned_data['Sname']
                P=STDO.cleaned_data['Password']
                RP=STDO.cleaned_data['Reenterpassword']
                E=STDO.cleaned_data['Email']
                RE=STDO.cleaned_data['ReenterEmail']
                STF=Student_model.objects.get_or_create(Sname=Sn,Password=P,Reenterpassword=RP,Email=E,ReenterEmail=RE)[0]
                STF.save()
                return HttpResponse('Data can be created')
          else:
               return HttpResponse('Invalid Data')
    return render(request,'create_studentform.html',d)






