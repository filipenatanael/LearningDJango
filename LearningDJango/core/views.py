from django.shortcuts import render
from django.http import HttpResponse
from LearningDJango.Courses.models import Course

def home(request):
    return render(request, 'home.html', {'username': 'Filipe'})
    # return HttpResponse('Hello World!!!')

def contact(request):
    return render(request, 'contact.html',  {'email': 'email@exemple.com'})

def courses(request):
    course = Course.objects.all()
    template_name = 'courses.html'
    context = {
        'courses': course
    }
    return render(request, template_name, context)
