from django.shortcuts import render
from .models import *


# Create your views here.

def national(request):
    national = National.objects.all()
    context = {'national': national}  
    return render(request, 'office/national.html', context)


def ujkz(request):
    ujkz = UJKZ.objects.all()
    context = {'ujkz': ujkz}  
    return render(request, 'office/ujkz.html', context)


def usta(request):
    usta = USTA.objects.all()
    context = {'usta': usta}  
    return render(request, 'office/usta.html', context)


def inssa(request):
    inssa = INSSA.objects.all()
    context = {'inssa': inssa}  
    return render(request, 'office/inssa.html', context)


def uohg(request):
    uohg= UOHG.objects.all()
    context = {'uohg': uohg}  
    return render(request, 'office/uohg.html', context)


def usdao(request):
    usdao = USDAO.objects.all()
    context = {'usdao': usdao}  
    return render(request, 'office/usdao.html', context)

