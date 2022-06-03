from django.db import models

# Create your models here.

class Employees(models.Model):
    e_id = models.AutoField(primary_key=True) # unique id for each employee
    username = models.CharField(max_length=50) # username and password used to login
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50) # name of the employee


    def __str__(self):
        return self.name

class Customers(models.Model):
    c_id = models.AutoField(primary_key=True) # unique id for each customer
    name = models.CharField(max_length=50) # name of the distributor company
    address = models.CharField(max_length=50) # address of the customer
    phone = models.CharField(max_length=50) # phone number of the customer
    # authentication variables
    public_key = models.CharField(max_length=50) # key used to authenticate the user
    private_key = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Products(models.Model):
    p_id = models.AutoField(primary_key=True) # unique id for each product
    category = models.CharField(max_length=50) # category of the product
    p_name = models.CharField(max_length=50) # name of the product within a category
    package_size = models.CharField(max_length=20) # package size of the product
    price = models.CharField(max_length=20) # price of the product
    dimensions = models.CharField(max_length=20) # dimensions of the product
    stock = models.CharField(max_length=20) # stock of the product

    def __str__(self):
        return self.name

class Orders(models.Model):
    o_id = models.AutoField(primary_key=True) # unique id for each order
    c_id = models.CharField(max_length=50) # customer id
    e_id = models.CharField(max_length=50) # employee id
    cart = models.JSONField(Products) # cart of the order, here we list the products as an array 
    price = models.CharField(max_length=20) # price of the product
    date = models.CharField(max_length=20) # date of the order
    status = models.CharField(max_length=20) # status of the order

    def __str__(self):
        return self.name
