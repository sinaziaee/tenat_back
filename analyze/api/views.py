from django.shortcuts import render, HttpResponse


def home_api(request):
    return HttpResponse('apis')
