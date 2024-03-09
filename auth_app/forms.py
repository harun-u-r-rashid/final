from django import forms
from .models import Account
from django.core import validators




class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter your username",
        'class' : 'form-control'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter your first name",
        'class' : 'form-control'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter your last name",
        'class' : 'form-control'
    }))
    
    picture = forms.ImageField(required=False)
    
    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter your phone number",
        'class' : 'form-control'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : "Enter your first name",
        'class' : 'form-control'
    }))
    
    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder' : "Enter password",
        'class' : 'form-control'
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password',
        'class' : 'form-control'
    }))
    
    
    class Meta:
        model = Account
        fields = ['username','first_name', 'last_name', 'phone_number', 'email','picture', 'password']
        
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('password')
        
        
        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
            
        return cleaned_data
            
            
          
 
class ChangeUserDataForm(forms.ModelForm):
    password = None
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter your first name",
        'class' : 'form-control'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter your last name",
        'class' : 'form-control'
    }))
    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter your phone number",
        'class' : 'form-control'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : "Enter your first name",
        'class' : 'form-control'
    }))
    
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email']
        
