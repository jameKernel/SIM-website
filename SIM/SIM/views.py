from django.http import request, response
from django.shortcuts import render
from django.template import response


def home(request):
    context = {}
    return render(request, 'index/index.html', context=context)
