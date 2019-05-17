from django.shortcuts import render
from django.http import HttpResponse
from Practiceapp.models import Employee
from . import forms
# Create your views here.

def Practice(request):
    return HttpResponse('<h1>this is normal view</h1>')

def normalh(request):
    return render(request,'PracticeDemoapp/Practice.html')

def ret(request):
    e=Employee.objects.all()
    return render(request,'PracticeDemoapp/Practice.html',{'e':e})
def Demo(request):
    form=forms.Employee()
    if request.method=='POST':
        form=forms.Employee(request.POST)
        if form.is_valid():
            form.save()
            return thankyou(request)
    return render(request,'practiceDemoapp/Demo.html',{'form':form})

def thankyou(request):
    return render(request,'PracticeDemoapp/thank.html')
