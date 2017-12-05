"""
This view was created only to test our Django application.
Here we have a simple function based view (home_page)
"""

from django.http import HttpResponse
from django.shortcuts import render



# Functio based view 
def home_page(request):
    return HttpResponse("<h1>Hello Universe!!!</h1>")
