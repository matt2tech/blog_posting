from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from . import forms
from app import models

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html', {'Blogs': models.BlogPost.objects.all()})

class BlogCreate(View):
    def get(self, request):
        return render(request, 'blog_create.html', {'form': forms.BCreateForm()})

    def post(self, request):
        form = forms.BCreateForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            body = form.cleaned_data['body']
            cover_image = form.cleaned_data['cover_image']
            models.BlogPost.submitted(title, body, author, cover_image)
            return redirect('home')
        else:
            return render(request, 'blog_create.html', {'form': form})

class BlogDetail(View):
    def get(self, request, id):
        return render(request, 'blog_detail.html', {'blog': models.BlogPost.objects.get(id=id)})
