from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.decorators import api_view, parser_classes
#database and json serializers
# from database.models import Employees , Customers , Products , Orders
from .models import Products
from database.serializers import UserSerializer, ProductSerializer
from django.contrib.auth import get_user_model

from main.decorators import employee_required

# only for developement purposes, do not use in production
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

@api_view(['GET', 'POST'])
@parser_classes((MultiPartParser, FormParser))
@csrf_exempt
def product_list(request, pk=None):
    """
    GET: List all products
    GET <pk>: Get a product by id
    """
    # any user, authenticated or not, can access this api
    if request.method == 'GET':
        if pk is not None:
            products = Products.objects.filter(product_id=pk)
        else:
            products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
       
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            json = {
                "message": "Product created successfully",
                "errors" : False
            }
            return JsonResponse(json, status=201)

@employee_required
@csrf_exempt
def client_list(request, pk=None):
    """
    List all clients.
    """
    # if request.user.is_authenticated and request.user.is_employee or request.user.is_superuser:
    if request.method == 'GET':
        if pk is not None:
            clients = get_user_model().objects.filter(is_client__in=[True], id=pk).values('id', 'email', 'name','address', 'phone')
        else:
            clients = get_user_model().objects.filter(is_client__in=[True]).values('id', 'email', 'name','address', 'phone')

        serializer = UserSerializer(clients, many=True)
        
        return JsonResponse(serializer.data, safe=False)
    # return JsonResponse({"error": True, "message":"You are not authorized to do this."}, safe=False)
        # only authenticated employees or admins can create products
        # if not request.user.is_authenticated and not (request.user.is_employee or request.user.is_admin):
        #     data = JSONParser().parse(request)
        #     serializer = ProductSerializer(data=data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         json = {
        #             "error":False,
        #             "message": "Succesfully added product"
        #             }
        #         return JsonResponse(json, status=200)
        #     json = {
        #         "error":True,
        #         "message": "Error adding product"
        #         }
        #     return JsonResponse(json, status=400)
        # json = {
        #     "error":True,
        #     "message": "You are not authorized to add products"
        #     }
        # return JsonResponse(json, status=401)




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
    