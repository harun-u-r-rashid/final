
from django.shortcuts import render, redirect
from . import models
from . import forms
from django.http import HttpResponse 





def add_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            addblog_form = forms.BlogForm(request.POST, request.FILES)
            if addblog_form.is_valid():
                addblog_form.save()
                return redirect('show_blog')
        else:
            addblog_form = forms.BlogForm()
            
        return render(request, 'appBlog/add_blog.html', {'addblog_form':addblog_form})
    return HttpResponse("<h3>Only users can add a blog!</h3>")



def show_blog(request):
    blog = models.Blog.objects.all()
    
    return render(request, 'appBlog/show_blog.html', {'blog':blog})


                                           