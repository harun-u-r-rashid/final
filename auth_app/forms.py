from django import forms
from .models import Account
from django.core import validators




class RegistrationForm(forms.ModelForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    'type': 'text',
    'placeholder': 'Username'
}))


    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        
        'placeholder':'First Name'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        
        'placeholder': 'Last Name'
    }))

    
    
    
    picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control',
      
    }))
    
    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
      
        'placeholder': 'Phone Number'
    }))


    
    email = forms.CharField(widget=forms.EmailInput(attrs={
       'class': 'form-control',
        'type': 'email',
        'placeholder': 'Email'
    }))
    
    password = forms.CharField(widget = forms.PasswordInput(attrs={
       'class': 'form-control',
        'type': 'password',
        
        'placeholder': 'Password'
    }))
    
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
       
        'placeholder': 'Confirm Password'
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
    
    picture = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control'
    }))
    
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name','picture', 'phone_number', 'email']
        
