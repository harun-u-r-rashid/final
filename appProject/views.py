from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms
from django.http import HttpResponse 
from django.db.models import Avg


def add_project(request):
    if request.user.is_authenticated:
        if request.method == 'POST': 
            project = forms.ProjectForm(request.POST, request.FILES)
            if project.is_valid():
                project.save()
                print(project.cleaned_data)
                return redirect('show_project')
        else:
            project = forms.ProjectForm()
        return render(request, 'appProject/add_project.html', {'project': project})
    return HttpResponse("<h3>Only users can add project!</h3>") 


def show_project(request):
    project = models.Project.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')
    return render(request, 'appProject/show_project.html', {'project': project})




def project_details(request, title):
    project_details = get_object_or_404(models.Project, pk=title)
    reviews = project_details.reviews.all()
    print(reviews)
    return render(request, 'appProject/project_details.html', {'project_details':project_details, 'reviews':reviews})


   
def project_review(request):
    if request.method == 'POST':
        review = forms.ProjectReviewForm(request.POST)
        if review.is_valid():
            review.save()
            print(review.cleaned_data)
            return redirect('show_project')
    else:
        review = forms.ProjectReviewForm()
    return render(request, 'appProject/project_review.html', {'review':review})
  
  

    