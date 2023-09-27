from django.shortcuts import render, redirect  
from studentdetails.forms import StudentForm  
from studentdetails.models import studentDetails

def student(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'index.html',{'form':form}) 


def show(request):  
    students = studentDetails.objects.all()  
    return render(request,"show.html",{'students':students}) 