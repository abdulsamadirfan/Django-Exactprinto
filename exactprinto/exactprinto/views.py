from django.shortcuts import render
from django.http import HttpResponse
# Create your tests here.
def index(request):
    return   render(request, 'index.html')