from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {'username': 'Filipe'})
    # return HttpResponse('Hello World!!!')

def contact(request):
    emails = ['Learning@homail.com','Learning@gmail.com']
    return render(request, 'contact.html', emails)
    #return render(request, 'contact.html',  {'email':'email@exemple.com'})
