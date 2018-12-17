from django.forms import Form
from django import forms

class BCreateForms(Form):
    title = forms.CharField(label='Title')
    author = forms.CharField(label='Author')
    body = forms.Textarea(label='Blog')
    cover_image = forms.URLField(label="Cover Image")
