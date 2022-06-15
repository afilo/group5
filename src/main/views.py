
from django.contrib.auth import get_user_model, authenticate, login, logout as django_logout
User = get_user_model()

# normal methods for views
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

# rest api methods for views
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# database

# decorators for forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import EmployeeCreateForm, EmployeeLoginForm, AddProductForm
from database.models import Products



def index(request):
    return render(request, 'client/client.html')


def login_client(request):
    return render(request, 'client/login.html')

def login_employee(request):
    # if employee is already authenticated, redirect to employee home
    if request.user.is_authenticated:
        return redirect('/employee/')


    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("/employee/")

    form = EmployeeLoginForm()
    return render(request, 'employee/login.html', {'form': form})

def logout(request):
    type = ''
    if request.user.is_employee:
        type = 'employee/'
    elif request.user.is_superuser:
        type = 'admin/'
    
    # have to do same if we create admin
    django_logout(request)
    return redirect(f'/{type}login')


    #         if user is not None:
    #             login(request, user)
    #             return redirect('/employee/')
    #         else:
    #             msg = 'Error: Invalid email or password!'
    #     else:
    #         msg = 'Error: Invalid email or password!'
    # else:
    #     form = EmployeeLoginForm()
    #     return render(request, 'employee/login.html', {'form': form, 'msg': msg})

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
            return redirect('/employee')
        msg = 'Error: Employee was not created!'
    else:
        form = EmployeeCreateForm()
    return render(request, 'employee/register.html', {'form': form, 'msg': msg})

def profile_employee(request):
    last_login = request.user.last_login
    return render(request, 'employee/profile.html', {'last_login': last_login})

def products_employee(request):
    products = Products.objects.all()
    return render(request, 'employee/products.html', {'products': products})

def products_employee_create(request):
    msg = None
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('/employee/products')
        msg = 'Error: Product was not created!'
    else:
        form = AddProductForm()
    return render(request, 'employee/products_create.html', {'form': form, 'msg': msg})

def employee_home(request):
    return render(request, 'employee/index.html')


def create_client(request):
    return render(request, 'client/register.html')

