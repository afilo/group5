
from django.contrib.auth import get_user_model
User = get_user_model()

# normal methods for views
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

# rest api methods for views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# database

# decorators for forms
from django.contrib.auth.forms import UserCreationForm
from .forms import EmployeeCreateForm

def index(request):
    return render(request, 'client/client.html')


def login_client(request):
    return render(request, 'client/login.html')

def login_employee(request):
    return render(request, 'employee/login.html')

# def create_employee(request):

#     if request.method == 'POST':
#         form = EmployeeSignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/employee/login')
#         return HttpResponse('Employee was not created!')
#     else:
#         form = EmployeeSignUpForm()
#         return render(request, 'employee/register.html', {'form': form})


def create_employee(request):
    msg = None
    if request.method == 'POST':
        form = EmployeeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_employee)
        msg = 'Error: Employee was not created!'
    else:
        form = EmployeeCreateForm()
    return render(request, 'employee/register.html', {'form': form, 'msg': msg})


def login_emplyee(request):
    return render(request, 'employee/login.html')