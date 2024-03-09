from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from . models import Contact, Skill, Blog,  Project ,Resume,ProjectReview 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import BlogForm, SkillForm,  ProjectForm, ContactForm, ProjectReviewForm
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.db.models import Avg



def home(request):
    return render(request,'portfolio_app/home.html')

def about(request):
    return render(request, 'portfolio_app/about.html')





def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request, "Thanks for contacting us!")
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'portfolio_app/contact.html', {'form' : form})

        
    
     


def add_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                form.save()
                print(form.cleaned_data)
                return redirect('show_blog')
        else:
            form = BlogForm()
            
        return render(request, 'portfolio_app/add_blog.html', {'form':form})
    return HttpResponse("<h3>Only users can add a blog!</h3>")



def show_blog(request):
    blog = Blog.objects.all()
    print(blog)
    return render(request, 'portfolio_app/show_blog.html', {'blog':blog})




def add_skill(request):
    skill = ""
    if request.user.is_authenticated:
        if request.method == 'POST':
            skill= SkillForm(request.POST)
            if skill.is_valid():
                skill.save()
                print(skill.cleaned_data)
                return redirect('show_skill')
        else:
            skill = SkillForm()
            
        return render(request, 'portfolio_app/add_skill.html', {'skill':skill})
    return HttpResponse("<h3>Only users can add a skill!</h3>")

 



def show_skill(request):
    skill = Skill.objects.all()
    print(skill)
    return render(request, 'portfolio_app/show_skill.html', {'skill':skill})

   
   
   

def add_project(request):
    if request.user.is_authenticated:
        if request.method == 'POST': 
            project = ProjectForm(request.POST, request.FILES)
            if project.is_valid():
                project.save()
                print(project.cleaned_data)
                return redirect('show_project')
        else:
            project = ProjectForm()
        return render(request, 'portfolio_app/add_project.html', {'project': project})
    return HttpResponse("<h3>Only users can add project!</h3>") 


def show_project(request):
    project = Project.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')
    return render(request, 'portfolio_app/show_project.html', {'project': project})




def project_details(request, title):
    project_details = get_object_or_404(Project, pk=title)
    return render(request, 'portfolio_app/project_details.html', {'project_details':project_details})

   
def project_review(request):
    if request.method == 'POST':
        review = ProjectReviewForm(request.POST)
        if review.is_valid():
            review.save()
            print(review.cleaned_data)
            return redirect('show_project')
    else:
        review = ProjectReviewForm()
    return render(request, 'portfolio_app/project_review.html', {'review':review})
  
    
    
def download_resume(request):
    resume = get_object_or_404(Resume)
    response = HttpResponse(resume.file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    return response

