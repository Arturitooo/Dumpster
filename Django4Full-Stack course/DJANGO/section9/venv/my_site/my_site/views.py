from django.shortcuts import render
from django.http.response import HttpResponse


def home_view(request):
    return HttpResponse("Home view!")
