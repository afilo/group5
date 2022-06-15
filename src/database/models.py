from djongo import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_employee(self, email, name, phone, password , **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have a name')
        # if not username:
        #     raise ValueError('Users must have a username')

        extra_fields.setdefault('is_employee', True)
            
        user = self.model(
            email=self.normalize_email(email),
            name = name,
            phone = phone,
            is_employee = True,
            **extra_fields
            )
        user.set_password(password)
        user.save()

        return user

    def create_client(self, email, name, password , **extra_fields):    
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have a name')
        # if not username:
        #     raise ValueError('Users must have a username')
        
        user = self.model(
            email=self.normalize_email(email),
            name = name,
            is_client = True,
            **extra_fields
            )
        user.set_password(password)
        user.save()

        return user


    def create_user(self, email, name, password, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have a name')
        # if not username:
        #     raise ValueError('Users must have a username')
        
        user = self.model(
            email=self.normalize_email(email),
            name = name,
            **extra_fields
            )
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email,name, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)


        """Creates and saves a new superuser"""
        user = self.create_user(email, name, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user



class custom_User(AbstractBaseUser, PermissionsMixin):
    # roles
    is_employee = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    # entry data
    email = models.EmailField(unique=True)
    # username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    def __str__(self):
        return self.name



# class Admin(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     email = models.EmailField()
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.username


# class Employees(models.Model):
#     # needed to create user model
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     name = models.CharField(max_length=50) # name of the employee
#     email = models.EmailField()
#     phone = models.CharField(max_length=15) # phone number of the employee
#     # authentication
#     username = models.CharField(max_length=50) 
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


# class Customers(models.Model):
#     # needed to create user model
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     c_id = models.AutoField(primary_key=True) # unique id for each customer
#     name = models.CharField(max_length=50) # name of the distributor company
#     email = models.EmailField() # email of the distributor company
#     address = models.CharField(max_length=100) # address of the customer
#     phone = models.CharField(max_length=15) # phone number of the customer
#     cart = models.ArrayReferenceField(to='Orders',) # array of cart objects
#     # authentication
#     username = models.CharField(max_length=50) 
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name



class Products(models.Model):
    product_id = models.AutoField(primary_key=True) # id for a product
    title = models.CharField(max_length=100) # title to show 
    description = models.TextField() # description that shows under title
    price = models.IntegerField() # price for this product
    image = models.ImageField(upload_to='products/',default="nophoto.png") # images
    box_quantity = models.IntegerField() # number of items in the box
    box_weight = models.IntegerField() # weight of the box in grams
    box_dimensions = models.CharField(max_length=100,default="-") # dimensions of the box
    stock = models.IntegerField(default=0) # number of items in stock

    def __str__(self):
        return self.title

class Production(models.Model):
    pass
    # date = models.DateField() # date of the production
    # quantity = models.IntegerField() # quantity of the product produced


# create a cart class to hold a single data for the actual cart
class Cart(models.Model):
    pass
    # product = models.EmbeddedField(Products, on_delete=models.CASCADE) # product in the cart
    # quantity = models.IntegerField() # quantity of the product in the cart
    # price = models.DecimalField(max_digits=10, decimal_places=2) # price of the product in the cart

    # class Meta:
    #     abstract = True


# orders will have this structure
# this will also be used to create temporary carts with the DRAFTED option
# if user logins and has a DRAFTED order, it will be loaded by default into the cart
class Orders(models.Model):
    pass
    # ACCEPTEDED = 'AC'
    # PENDING = 'PE'
    # CANCELLED = 'CA'
    # DRAFTED = 'DR'

    # customer = models.ArrayReferenceField(to=custom_User) # customer who placed the order
    # employee = models.ArrayReferenceField(to=custom_User) # employee who processed the order
    # date = models.DateField() # date of the order
    # state = models.CharField(max_length=2, 
    #     choices=[
    #         (ACCEPTEDED, 'Accepted'),
    #         (PENDING, 'Pending'),
    #         (CANCELLED, 'Cancelled'),
    #         (DRAFTED, 'Drafted')
    #         ]) # state of the order
    # cart = models.ArrayField(model_container=Cart) # array of products in the order
    # total = models.CharField(max_length=20) # total price of the order

    # def __str__(self):
    #     return self.cart
