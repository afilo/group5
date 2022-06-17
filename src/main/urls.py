from django.urls import path, re_path
from . import views
from database import views as database_views


urlpatterns = [
    # employee endpoints
    path('employee/', views.employee_home, name="Employee Index"),
    path('employee/login', views.login_employee, name="Employee Login"),
    path('employee/create', views.create_employee, name="Create Employee"),
    path('employee/profile', views.profile_employee, name="Employee Logout"),
    path('employee/products', views.products_employee, name="Employee Products"),
    path('employee/products/create', views.products_employee_create, name="Employee Products Create"),
    path('employee/clients', views.clients_employee, name="Client List"),
    path('employee/clients/create', views.clients_employee_create, name="Client Create"),
    path('employee/orders', views.orders_employee, name="Order List"),
    path('employee/factory', views.factory_employee, name="Factory List"),
    path('employee/magazine', views.magazine_employee, name="Magazine List"),
    path('employee/', views.employee_home, name="Employee Index"),


    path('login',views.login_user, name="Login"),
    # client endpoints
    path('',views.index, name="Home Page"),
    path('profile', views.profile_user, name="Profile"),
    path('products/<int:id>', views.products_user, name="Products"),

    path('logout', views.logout, name="Logout"),
    

    # api endpoints
    path('api/user', database_views.user_list, name="User List"),
    path('api/user/<int:pk>', database_views.user_list, name="User Detail"),
    path('api/products', database_views.product_list, name="Product List"),
    path('api/products/<int:pk>', database_views.product_list, name="Product Detail"),
    path('api/clients', database_views.client_list, name="Client List"),
    path('api/clients/<int:pk>', database_views.client_list, name="Client Detail"),
]
