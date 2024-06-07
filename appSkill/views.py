from django.shortcuts import render, redirect
from . import models
from . import forms
from django.http import HttpResponse 




def add_skill(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            skill = forms.SkillForm(request.POST, request.FILES)
            if skill.is_valid():
                skill.save()
                return redirect('show_skill')
        else:
            skill = forms.SkillForm()
            
        return render(request, 'appSkill/add_skill.html', {'skill': skill})
    return HttpResponse("<h3>Only users can add a skill!</h3>")

 



def show_skill(request):
    skill = models.Skill.objects.all()
    print(skill)
    return render(request, 'appSkill/show_skill.html', {'skill':skill})

   
   