from django.shortcuts import render
# from .models import *

def test(request):
    return render(request, 'categories/index.html')

def sub_test(request):
    return render(request, 'sub_categories/index.html')

def rahim(request):
    return render(request, 'sub_categories/index.html')


# def test(request):
#     return render(request, 'sub_categories/index.html')