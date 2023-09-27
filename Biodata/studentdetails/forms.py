from django import forms  
from studentdetails.models import studentDetails
from django.forms import fields

class StudentForm(forms.ModelForm):  
    class Meta:  
        model = studentDetails  
        fields = "__all__"