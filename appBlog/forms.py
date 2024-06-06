
from django import forms
from . import models

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
        model = models.Blog
        fields = ['author', 'title', 'content', 'image']


