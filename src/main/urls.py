from django.urls import path, re_path
from . import views
from database import views as database_views


urlpatterns = [
    
    path('employee/', views.employee_home, name="Employee Index"),
    path('employee/login', views.login_employee, name="Employee Login"),
    path('employee/create', views.create_employee, name="Create Employee"),
    path('employee/profile', views.profile_employee, name="Employee Logout"),
    path('employee/products', views.products_employee, name="Employee Products"),
    path('employee/products/create', views.products_employee_create, name="Employee Products Create"),

    path('',views.index, name="Home Page"),
    path('client/login', views.login_client, name="Client Login"),
    path('client/create', views.create_client, name="Create Client"),
    

    path('logout', views.logout, name="Logout"),
    # api endpoints
    path('api/user', database_views.user_list, name="User List"),
    path('api/user/<int:pk>', database_views.user_list, name="User Detail"),
    path('api/products', database_views.product_list, name="Product List"),
    path('api/products/<int:pk>', database_views.product_list, name="Product Detail"),
]
