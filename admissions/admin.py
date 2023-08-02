from django.contrib import admin

# Register your models here.
from admissions.models import Student

class showAttributes(admin.ModelAdmin):
    list_display = ['name','fathername','classname','contact']

admin.site.register(Student,showAttributes)