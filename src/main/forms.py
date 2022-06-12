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

class EmployeeLoginForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, required=True, label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = get_user_model()
        fields = ('email','password')

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise forms.ValidationError('User does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Password is incorrect')

        return super(EmployeeLoginForm, self).clean(*args, **kwargs)



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






