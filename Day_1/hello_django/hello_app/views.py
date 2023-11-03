from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_hello(request):
    sat_scores={
        'name':'Mike',
        'course' : 'Flutter',
        'marks' : 45
    }
    return render(request, 'hello.html', sat_scores)
    # return HttpResponse("<b>hello django</b>")
