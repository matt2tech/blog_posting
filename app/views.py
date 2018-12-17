from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
# from . import forms
from app import models

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html', {'Blogs': models.BlogPost.objects.all()})

class BlogCreate(View):
    def get(self, request):
        return render(request, 'blog_create.html', {'forms': forms.BCreateForms()})
