from django.urls import path, re_path
from . import views

urlpatterns = [
    # re_path(r'^department$', views.departmentApi),
    # re_path(r'^department/([0-9]+)$', views.departmentApi),
    path('',views.index, name="Employe main menu"),

    re_path(r'^employees$', views.employeeApi),
    re_path(r'^employees/([0-9]+)$', views.employeeApi),
    
]
