"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admissions.views import *
from finance.views import *
from django.contrib.auth.decorators import login_required
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/',include('django.contrib.auth.urls')),
    
    path('',home, name='home'),
    path('addAdmission/',addAdmission, name='addAdmission'),
    path('admissionsReport/',admissionsReport, name='admissionsReport'),
    path('finance/',finance, name='finance'),
    path('all_finance/',all_finance, name='all_finance'),
    path('financeReports/',financeReports,name='financeReports'),
    path('vendor-details/',Vender,name='Vender'),
    path('delete/<int:id>/',deleteStudent,name='deleteStudent'),
    path('update/<int:id>/',updateStudent,name='updateStudent'),


    path('firstcbv/',login_required(FirstClassBasedView.as_view())),
    path('getteacher/', login_required(Teacherlist.as_view()),name='getteacherlist'),
    path('getteacher/<int:pk>', login_required(GetTeacher.as_view())),
    path('addteacher/',login_required(AddTeacher.as_view())),
    path('updateteacher/<int:pk>',login_required(UpdateTeacher.as_view())),
    path('deleteteacher/<int:pk>',login_required(DeleteTeacher.as_view())),


]