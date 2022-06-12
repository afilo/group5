from django.urls import path, re_path
from . import views
from database import views as database_views


urlpatterns = [
    
    path('employee/', views.employee_home, name="Employee Index"),
    path('employee/login', views.login_employee, name="Employee Login"),
    path('employee/create', views.create_employee, name="Create Employee"),
    path('logout', views.logout_employee, name="Logout"),

    path('',views.index, name="Home Page"),
    path('client/login', views.login_client, name="Client Login"),
    path('client/create', views.create_client, name="Create Client"),
    
    # api endpoints
    path('api/user', database_views.user_list, name="User List"),
    path('api/user/<int:pk>', database_views.user_list, name="User Detail"),

]
