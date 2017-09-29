from django.shortcuts import render

# Create your views here.

def Courses(request):
    template_name = 'Courses/cources.html'
    return render(request, template_name)