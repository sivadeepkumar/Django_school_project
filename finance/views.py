from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def finance(request):
    return render(request,'finance.html')


def all_finance(request):
    return render(request,'all_finance.html')


def financeReports(request):
    return render(request,'financeReports.html')

