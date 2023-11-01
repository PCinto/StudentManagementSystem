from django.shortcuts import render
from student.forms import EmployeeForm
from student.models import Employee




# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request, 'login.html')

def details(request):
    return render(request, 'details.html')


def join(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,   'join.html')
        else:
            return render(request,  'join.html')

def detail(request):
    members = Employee.objects.all()
    return render(request,  'detail.html',  {'all':members})