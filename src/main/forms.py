from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class EmployeeCreateForm(UserCreationForm):
    
    email = forms.EmailField(max_length=100, required=True, label='Email')
    name = forms.CharField(max_length=100, required=True, label='Name')
    username = forms.CharField(max_length=100, required=True, label='Username')
    phone = forms.CharField(max_length=100, required=True, label='Phone')

    class Meta:
        model = get_user_model()
        fields = ('name','email','phone','username','password1','password2')

    def save(self, commit=True):    
        user = super().save(commit=False)
        user.is_employee = True

        if commit:
            user.save()
        return user

# class EmployeeSignUpForm(UserCreationForm):
#     name = forms.CharField(max_length=50, required=True, label='Full Name')
#     email = forms.EmailField(required=True, label="Email")
#     phone = forms.CharField(max_length=15, required=True, label="Phone Number")

#     class Meta:
#         model = Employees
#         fields = ['name','email','phone','username', 'password1', 'password2']
    
#     def save(self, commit=True):
#         user = super(EmployeeSignUpForm, self).save(commit=False)
#         user.is_employee = True
#         if commit:
#             user.save()
#         return user


class CustomerSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True, label='Full Name')
    email = forms.EmailField(required=True, label="Email")
    address = forms.CharField(max_length=100, required=False, label="Address")
    phone = forms.CharField(max_length=15, required=True, label="Phone Number")
    
    class Meta:
        model = get_user_model()
        fields = ['name','email','address','phone','username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CustomerSignUpForm, self).save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
        return user


class AdminSignUpForm(UserCreationForm):
 
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CustomerSignUpForm, self).save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user




