from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def top_page(request):
    return HttpResponse("New warzone developping now!")
