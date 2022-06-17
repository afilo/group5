from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate, login

from database.models import Products

class EmployeeCreateForm(UserCreationForm):
    
    email = forms.EmailField(max_length=100, required=True, label='Email')
    name = forms.CharField(max_length=100, required=True, label='Name')
    # username = forms.CharField(max_length=100, required=True, label='Username')
    phone = forms.CharField(max_length=100, required=True, label='Phone')

    class Meta:
        model = get_user_model()
        fields = ('name','email','phone','password1','password2')

    def save(self, commit=True):    
        user = super().save(commit=False)
        user.is_employee = True

        if commit:
            user.save()
        return user

class EmployeeLoginForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Wrong email or password')
            if not user.check_password(password):
                raise forms.ValidationError('Wrong email or password')
        return super(EmployeeLoginForm, self).clean(*args, **kwargs)

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True, label='Email')
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise forms.ValidationError('User does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Password is incorrect')

        return super(LoginForm, self).clean(*args, **kwargs)

class ClientCreateForm(UserCreationForm):
        
        email = forms.EmailField(max_length=100, required=True, label='Email')
        name = forms.CharField(max_length=100, required=True, label='Name')
        # username = forms.CharField(max_length=100, required=True, label='Username')
        phone = forms.CharField(max_length=100, required=True, label='Phone')
        address = forms.CharField(max_length=100, required=False, label='Address')


        class Meta:
            model = get_user_model()
            fields = ('name','email','phone','address','password1','password2')
    
        def save(self, commit=True):    
            user = super().save(commit=False)
            user.is_client = True
    
            if commit:
                user.save()
            return user

class ClientLoginForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True, label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise forms.ValidationError('User does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Password is incorrect')

        return super(ClientLoginForm, self).clean(*args, **kwargs)


class AddProductForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True, label='Title')
    description = forms.CharField(max_length=100, label='Description')
    price = forms.IntegerField(required=True, label='Price')
    box_quantity = forms.IntegerField(required=True, label='Box Quantity')
    box_weight = forms.IntegerField(required=True, label='Box Weight')
    box_dimensions = forms.CharField(max_length=100, label='Box Dimensions')
    stock = forms.IntegerField( label='Current Stock')

    class Meta:
        model = Products
        fields = ('title','description','price','image','box_quantity','box_weight','box_dimensions','stock')


    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
        return product


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






