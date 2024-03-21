from typing import Any
from django import forms
from .constants import PROJECT_CATEGORY, RATING
from .models import Blog, Skill, Contact, Project , ProjectReview

class BlogForm(forms.ModelForm):
    title = forms.CharField(required = True, widget=forms.TextInput(attrs={
        'placeholder' : "Enter title",
        'class' : 'form-control'
    }))
    
    
    content = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter content",
        'class' : 'form-control'
    }))
    
    
    author = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter author",
        'class' : 'form-control'
    }))
    
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        
    }))
    
    create_date = forms.DateInput()
    
    
    class Meta:
        model = Blog
        fields = ['author', 'title', 'content', 'image']






class SkillForm(forms.ModelForm):
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter title",
        'class' : 'form-control'
    }))
    
    skill_category = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "skill Category..",
        'class' : 'form-control'
    }))
    
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Description..",
        'class' : 'form-control'
    }))
     
    class Meta:
        model = Skill
        fields = ['title', 'skill_category', 'description']
   
   

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Name...",
        'class' : 'form-control'
    }))
    
    email = forms.EmailField(widget = forms.EmailInput(attrs={
        'placeholder' : "Email...",
        'class' : 'form-control'
    }))
    
    number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder' : "Number...",
        'class' : 'form-control'
    })) 
    
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Description...",
        'class' : 'form-control'
    }))
    
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'description']
     
   
   
    
    
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
        model = Project   
        fields = ['title', 'project_category', 'description', 'technologies_used','image', 'url']
     
     
     
class ProjectReviewForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), 
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
        model = ProjectReview
        fields = ['project', 'rating', 'review']