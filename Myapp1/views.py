from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#MVC model controller view MVT -> model view template

def home(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())