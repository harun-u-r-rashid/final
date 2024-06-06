from typing import Any
from django import forms
from .constants import PROJECT_CATEGORY, RATING
from . import models


class ProjectForm(forms.ModelForm): 
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Title..",
        'class' : 'form-control',
        'maxlength': '30'
    }))

    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Description..",
        'class' : 'form-control',
         'maxlength': '200'
    }))
    
    technologies_used = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "echnology..",
        'class' : 'form-control',
        'maxlength': '150'
    }))
    
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={
        'class': 'form-control',
        
    }))
    
      
   
    
    url = forms.URLField(widget=forms.URLInput(attrs={
        'placeholder': 'Url..',
        'class': 'form-control'
    }))
    
      
   
    
    class Meta:
        model = models.Project   
        fields = ['title', 'project_category', 'description', 'technologies_used','image', 'url']
     
     
     
class ProjectReviewForm(forms.ModelForm):
   
    review = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Review..",
        'class' : 'form-control',
        'maxlength': '120'
    }))
    class Meta:
        model = models.ProjectReview
        fields = ['project', 'rating', 'review']