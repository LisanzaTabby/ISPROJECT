from django.shortcuts import render,redirect
from .models import *
from .forms import StudentForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    return render(request, 'index.html')
def signupView(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account successfully created!')
            return redirect('login')
    context ={'form':form}
    return render(request,'signup.html',context)
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admindash')
        else:
            messages.info(request, 'USERNAME or PASSWORD is Incorrect!')
        
    context = {}
    return render(request, 'login.html',context)
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
def logoutView(request):
    logout(request)
    return redirect('login')