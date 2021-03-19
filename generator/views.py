from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def koper(request):
    return render(request, 'generator/koper.html')

def password(request):

    characters = 'abcdefghijklmnopqrstuwxyz'

    if request.GET.get("Uppercase"):
        characters += characters.upper()
    if request.GET.get("Numbers"):
        characters += "1234567890"
    if request.GET.get("Special"):
        characters += "!@#$%^&*()_-<>?:\"'{}[];,./"

    alnums = list('abcdefghijklmnopqrstuwxyz1234567890')
    allchars = list('abcdefghijklmnopqrstuwxyz1234567890,.')
    length = int(request.GET.get('length',12))
    #password_type
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(list(characters))


    return render(request, 'generator/password.html', {'password':thepassword})
