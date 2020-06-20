from django.shortcuts import render
import random


# Create your views here.


def home(request):
    length = [6, 7, 8, 9, 10, 11, 12, 13, 14]
    return render(request, 'generator/home.html', {'length': length})


def about(request):
    return render(request, 'generator/about.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+|}{:<>?'))

    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
