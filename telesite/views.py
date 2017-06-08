from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def help1(request):
    return HttpResponse("Hello u r at help page")