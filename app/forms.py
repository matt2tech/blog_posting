from django.forms import Form
from django import forms

class BCreateForm(Form):
    title = forms.CharField(label='Title')
    author = forms.CharField(label='Author')
    body = forms.CharField(label='Body')
    cover_image = forms.URLField(label="Cover Image")

class CCreateForm(Form):
    title = forms.CharField(label='Title')
    author = forms.CharField(label='Author')
    body = forms.CharField(label='Body')
    rating = forms.IntegerField(min_value=1, max_value=5)
    
