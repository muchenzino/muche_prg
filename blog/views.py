from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def models_list(request):
    return HttpResponse("Testing of views")
