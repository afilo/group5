from rest_framework import serializers
from employee.models import Employees, Customers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeId', 'EmployeName', 'Deparament', 'DateOfJoining', 'PhotoFileName')        