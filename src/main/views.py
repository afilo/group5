
from distutils.log import Log
from django.contrib.auth import get_user_model, authenticate, login, logout as django_logout
User = get_user_model()
from main.decorators import employee_required


# normal methods for views
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

# rest api methods for views
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# database

# decorators for forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import EmployeeCreateForm, EmployeeLoginForm, AddProductForm, ClientCreateForm, ClientLoginForm, LoginForm
from database.models import Products



def index(request):
    if request.user.is_authenticated and request.user.is_employee:
        return redirect('/employee/')
    # the 3 most recent products to showcase on the homepage
    showcase = Products.objects.all().order_by('-product_id')[:3]
    
    # all products for sale
    products = Products.objects.all()
    return render(request, 'client/client.html', {'products': products, 'showcase': showcase})


def profile_user(request):
    return render(request, 'client/profile.html')

def products_user(request, id):
    product = Products.objects.get(product_id=id)
    return render(request, 'client/product.html', {'product': product})


# general login form for all users
def login_user(request):
    if request.user.is_authenticated and request.user.is_employee:
        return redirect('/employee/')
    elif request.user.is_authenticated and request.user.is_superuser:
        return redirect('/admin/')
    elif request.user.is_authenticated and request.user.is_client:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            if user.is_employee:
                return redirect('/employee/')
            elif user.is_superuser:
                return redirect('/admin/')
            return redirect('/')
    form = LoginForm()
    return render(request, 'client/login.html', {'form': form})

def login_client(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("/employee/")

    form = LoginForm()
    return render(request, 'employee/login.html', {'form': form})

def login_employee(request):
    # if employee is already authenticated, redirect to employee home
    


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
    
    django_logout(request)
    return redirect('/login')


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

# method for registering a new employee
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

# method to see current logged in employee profile
@employee_required
def profile_employee(request):
    last_login = request.user.last_login
    return render(request, 'employee/profile.html', {'last_login': last_login})

# list products that are in the database to the employee
@employee_required
def products_employee(request):
    products = Products.objects.all()
    return render(request, 'employee/products.html', {'products': products})

# create a new product from employee
@employee_required
def products_employee_create(request):
    form = AddProductForm()
    return render(request, 'employee/products_create.html', {'form': form})

# employee main menu
@employee_required
def employee_home(request):
    return render(request, 'employee/index.html')

# list clients that are in the database to the employee
# will use rest api to get all clients with fetch inside html
@employee_required
def clients_employee(request):
    clients = get_user_model().objects.filter(is_client__in=[True]).values('id', 'email', 'name','address', 'phone')

    return render(request, 'employee/clients.html', {'clients': clients})

# method for employee to add a new client

@employee_required
def clients_employee_create(request):
    msg = None
    if request.method == 'POST':
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Client was created successfully!'
        else:
            msg = 'Error: Client was not created!'
    else:
        form = ClientCreateForm()
    return render(request, 'employee/clients_create.html', {'form': form, 'msg': msg})

def orders_employee(request):
    return render(request, 'employee/orders.html')

def factory_employee(request):
    return render(request, 'employee/factory.html')

def magazine_employee(request):
    return render(request, 'employee/magazine.html')