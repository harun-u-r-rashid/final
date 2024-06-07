
from django import forms
from .models import Skill
class SkillForm(forms.ModelForm):
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Enter title",
        'class' : 'form-control',
        'maxlength': '30'

    }))
    
    skill_category = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "skill Category..",
        'class' : 'form-control',
        'maxlength': '100'
    }))
    
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Description..",
        'class' : 'form-control',
        'maxlength': '200'
    }))
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={
        'class': 'form-control',
        
    }))
     
    class Meta:
        model = Skill
        fields = ['title', 'skill_category', 'description', 'image']

   