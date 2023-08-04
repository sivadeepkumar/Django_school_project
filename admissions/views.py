from django.shortcuts import render,redirect
from admissions.models import Student,Teacher
from admissions.forms import StudentModelForm,VenderForm
from django.views.generic import View
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    return render(request,'index.html')


@login_required
def addAdmission(request):
    studentForm = {'form':StudentModelForm}
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request,'addAdmission.html',studentForm)

@login_required
def admissionsReport(request):
    result = Student.objects.all()
    students = {'allstudents':result}
    return render(request,'admissionsReport.html',students)


@login_required
def Vender(request):
    vform = {'form':VenderForm}
    if request.method == 'POST':
        form = VenderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return redirect('/')
        
    return render(request,'venderform.html',vform)

@login_required
def deleteStudent(request,id):
    d = Student.objects.get(id=id)

    d.delete()
    return redirect('/admissionsReport/')


@login_required
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
    fields = ('name','exp','subject','contact')


class UpdateTeacher(UpdateView):
    model = Teacher 
    fields = ('name','exp','subject','contact')
    # success_url = reverse_lazy('getteacherlist')


class DeleteTeacher(DeleteView):
    model = Teacher
    success_url = reverse_lazy('getteacherlist')    