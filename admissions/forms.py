from django import forms

from admissions.models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'



class VenderForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=100)
    item = forms.CharField(max_length=100)

    
