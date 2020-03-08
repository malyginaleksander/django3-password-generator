from django.shortcuts import render
import random
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse ('<h1> Hello, Aleksandr!</h1> ')
# def home(request):
#     return render (request, 'generator/home.html', {'password': 'mypassword'})
# def password(request):
#     return HttpResponse ('<h1> Eggs are so tasty...</h1> ')

def home(request):
    return render (request, 'generator/home.html')

def author(request):
    return render (request, 'generator/author.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get ('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get ('special'):
        characters.extend(list("!@#$%^&*()"))
    if request.GET.get ('numbers'):
        characters.extend(list("0123456789"))
    length = int(request.GET.get("length", 12))
    thepassword = ''
    for x in range (length):
        thepassword += random.choice(characters)
    return render (request, 'generator/password.html', {'password': thepassword })





