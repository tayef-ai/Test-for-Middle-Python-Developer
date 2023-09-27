from django.shortcuts import render, HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.db import connections

def homeview(request, id=None):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            roll = fm.cleaned_data['roll']
            address = fm.cleaned_data['address']
            mobile = fm.cleaned_data['mobile']
            cursor = connections['default'].cursor()
            cursor.execute("INSERT INTO studentapp_student (name, roll, address, mobile) VALUES( %s , %s, %s, %s )", [name, roll, address, mobile])
            fm = StudentForm()
    else:
        fm = StudentForm()
    stu = Student.objects.raw("SELECT * FROM studentapp_student")
    return render(request, 'index.html', {'context': stu, 'form': fm})

def deleteview(request, id):
    cursor = connections['default'].cursor()
    cursor.execute("DELETE FROM studentapp_student WHERE id=%s", [id])
    return HttpResponseRedirect('/')

def editview(request, id):
    if request.method == 'POST':
        dt = Student.objects.get(pk=id)
        fm = StudentForm(request.POST, instance=dt)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        dt = Student.objects.get(pk=id)
        fm = StudentForm(instance=dt)
    return render(request, 'updatestudent.html', {'form': fm})    