from typing import Any
from django import forms
from .constants import PROJECT_CATEGORY, RATING
from . import models


class ProjectForm(forms.ModelForm): 
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter title",
        'class' : 'form-control'
    }))

    project_category = forms.ChoiceField(choices=PROJECT_CATEGORY, widget=forms.Select(attrs={
        'placeholder' : "Select project category",
        'class' : 'form-control'
    }))
    
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter description",
        'class' : 'form-control'
    }))
    
    technologies_used = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter technology name that used",
        'class' : 'form-control'
    }))
    
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={
        'class': 'form-control',
        
    }))
    
      
   
    
    url = forms.URLField(widget=forms.URLInput(attrs={
        'placeholder': 'Enter URL',
        'class': 'form-control'
    }))
    
    class Meta:
        model = models.Project   
        fields = ['title', 'project_category', 'description', 'technologies_used','image', 'url']
     
     
     
class ProjectReviewForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=models.Project.objects.all(), 
                                     required=False,
                                     empty_label="Select project",
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    rating = forms.ChoiceField(choices=[(i, i) for i in range(0, 8)],
                               widget=forms.Select(attrs={
                                   'placeholder': 'Choose an image',
                                   'class': 'form-control',
                                   
                                   }))
    review = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter review",
        'class' : 'form-control'
    }))
    class Meta:
        model = models.ProjectReview
        fields = ['project', 'rating', 'review']