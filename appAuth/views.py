from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm, ChangeUserDataForm
from .models import Account
from . import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from . import models
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import forms
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.db.models import Avg




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
    return render(request, 'appAuth/register.html', {'form': form})
            
            
            
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
            return render(request, 'appAuth/login.html', {'login_form':login_form})
    messages.warning(request, "Please complete your registration!")
    return redirect('register')



def user_logout(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return render(request, 'appAuth/home.html')       
   
       
 
def show_user_profile(request):
    profile = Account.objects.all() 
    return render(request, 'appAuth/show_profile.html', {'profile':profile})



        
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
        return render(request, 'appAuth/edit_profile.html', {'form':form})
    
    else:
        return redirect('register')          
   
 





def contact(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request, "Thanks for contacting us!")
            return redirect('home')
    else:
        form = forms.ContactForm()
    return render(request, 'appAuth/contact.html', {'form' : form})

       


def home(request):
    return render(request,'appAuth/home.html')

def about(request):
    return render(request, 'appAuth/about.html')



    
def download_resume(request):
    resume = get_object_or_404(models.Resume)
    response = HttpResponse(resume.file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    return response


