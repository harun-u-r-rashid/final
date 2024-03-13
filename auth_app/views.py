from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm, ChangeUserDataForm
from .models import Account

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.picture = request.FILES.get('picture')
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'auth_app/register.html', {'form': form})
            
            
            
def user_login(request):
    if not request.user.is_authenticated:  
        if request.method == 'POST':
            login_form = AuthenticationForm(request=request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None: 
                    login(request, user)
                    messages.success(request, "Succeessfully loged in")
                    return redirect('home')
                    
        else:
            login_form = AuthenticationForm()
            return render(request, 'auth_app/login.html', {'login_form':login_form})
    messages.warning(request, "Please complete your registration!")
    return redirect('register')



def user_logout(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return render(request, 'portfolio_app/home.html')       
        
    
        
def user_profile_edit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserDataForm(request.POST, request.FILES, instance = request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Account updated successfully")
                return redirect('home')
        else:
            form = ChangeUserDataForm(instance = request.user)
        return render(request, 'auth_app/profile.html', {'form':form})
    
    else:
        return redirect('register')          
    