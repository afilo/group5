from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
#database and json serializers
# from database.models import Employees , Customers , Products , Orders
from database.serializers import UserSerializer
from django.contrib.auth import get_user_model

from main.decorators import employee_required


@csrf_exempt
def user_list(request, pk=None):
    """
    List all users.
    """
    if request.method == 'GET':
        if pk is not None:
            users = get_user_model().objects.filter(id=pk)
        else:
            users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)



# #require either employee or admin to access this view
# @employee_required
# @csrf_exempt
# def client_api(request, id=0):
#     # get all the clients
#     if request.method == 'GET':
#         customers = Customers.objects.all()
#         customers_serializer = CustomerSerializer(customers, many=True)
#         return JsonResponse(customers_serializer.data, safe=False)
    
#     # update a client
#     elif request.method == 'PUT':
#         customer_data = JSONParser().parse(request)
#         customer = Customers.objects.get(customerId=customer_data['customerId'])
#         customer_serializer = CustomerSerializer(customer, data=customer_data)
#         if customer_serializer.is_valid():
#             customer_serializer.save()
#             json_success = {
#                 'message': 'Customer updated successfully!',
#                 'stats': 'success',
#             }
#             return JsonResponse(json_success, safe=False)
#         json_fail = {
#             'message': 'Customer was not updated!',
#             'stats': 'error',
#         }
#         return JsonResponse(json_fail, safe=False)

#     # delete a client
#     elif request.method == 'DELETE':
#         customer = Customers.objects.get(customerId=id)
#         customer.delete()
#         json_success = {
#             'message': 'Customer deleted successfully',
#             'stats': 'success',
#         }
#         return JsonResponse("Customer deleted successfully", safe=False)



# @csrf_exempt
# def products_api(request, name):
#     if request.method == 'GET':
#         if name:
#             products = Products.objects.filter(p_name_contains=id)
#             products_serializer = ProductSerializer(products, many=True)
#             return JsonResponse(products_serializer.data, safe=False)
#         products = Products.objects.all()
#         products_serializer = ProductSerializer(products, many=True)
#         return JsonResponse(products_serializer.data, safe=False)
    