from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')
def student(request):
    students = Student.objects.all()
    context= {'students':students}
    return render(request, 'student.html', context)