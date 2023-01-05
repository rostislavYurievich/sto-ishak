from django.shortcuts import render
from django import template

def home(request):
    return render(request, 'templates/index.html')

def gallery(request):
    return render(request, 'templates/gallery.html')

def contacts(request):
    return render(request, 'templates/contacts.html')
