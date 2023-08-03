from django.shortcuts import render,redirect
from admissions.models import Student,Teacher
from admissions.forms import StudentModelForm,VenderForm
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView

# Create your views here.

def home(request):
    return render(request,'index.html')

def addAdmission(request):
    studentForm = {'form':StudentModelForm}
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request,'addAdmission.html',studentForm)


def admissionsReport(request):
    result = Student.objects.all()
    students = {'allstudents':result}
    return render(request,'admissionsReport.html',students)



def Vender(request):
    vform = {'form':VenderForm}
    if request.method == 'POST':
        form = VenderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return redirect('/')
        
    return render(request,'venderform.html',vform)


def deleteStudent(request,id):
    d = Student.objects.get(id=id)

    d.delete()
    return redirect('/admissionsReport/')



def updateStudent(request,id):
    u = Student.objects.get(id=id)
    form = StudentModelForm(instance=u)
    dict = {'form':form}
    if request.method == 'POST':
        form = StudentModelForm(request.POST,instance=u)
        if form.is_valid():
            form.save()
            return redirect('/admissionsReport')
    
    # return redirect('/admissionsReport/')
    return render(request,'updateStudent.html',dict)


class FirstClassBasedView(View):
    def get(self,request):
        return HttpResponse('<h1>First Class is Ready</h1>')
    


class Teacherlist(ListView):
    model = Teacher
    



class GetTeacher(DetailView):
    model = Teacher
    

class AddTeacher(CreateView):
    model = Teacher
    fields = ('name','subject','contact','exp')
