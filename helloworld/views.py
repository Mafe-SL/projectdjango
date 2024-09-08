from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("¡Hola Mundo desde Django!")

# Create your views here.
