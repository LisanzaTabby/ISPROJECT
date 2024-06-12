from django.shortcuts import render,redirect
from .models import *
from .forms import StudentForm
# Create your views here.
def index(request):
    return render(request, 'index.html')
def admindash(request):
    students = Student.objects.all()
    context= {'students':students}
    return render(request, 'admindash.html', context)
def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form =  StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admindash')

    context = {'form': form}
    return render(request, 'student_form.html', context)
def trusteeView(request):
    context = {}
    return render(request, 'trustee.html', context)
def DataEntryView(request):
    context = {}
    return render(request, 'dataentry.html', context)
def FinanceView(request):
    context = {}
    return render(request, 'finance.html', context)