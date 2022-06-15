from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate, login

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

        return super(EmployeeLoginForm, self).clean(*args, **kwargs)



class AddProductForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Title')
    description = forms.CharField(max_length=100, label='Description')
    price = forms.IntegerField(required=True, label='Price')
    image = forms.ImageField(required=True, label='Image')
    box_quantity = forms.IntegerField(required=True, label='Box Quantity')
    box_weight = forms.IntegerField(required=True, label='Box Weight')
    box_dimensions = forms.CharField(max_length=100, label='Box Dimensions')
    stock = forms.IntegerField( label='Current Stock')

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






