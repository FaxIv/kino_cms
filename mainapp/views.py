# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('mainapp/main.html')
    return HttpResponse(template.render())


def qwe(request):
    template = loader.get_template('mainapp/qwe.html')
    return HttpResponse(template.render())
