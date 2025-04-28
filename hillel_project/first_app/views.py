from django.shortcuts import render
from django.http import response

# Create your views here.
"""

MVT - model view template

"""


def hello(request):
    raise Exception
    return response.HttpResponse("<h2> Hello </h2> \n <a href='google.com'> Google </a>")