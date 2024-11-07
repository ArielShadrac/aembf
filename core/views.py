from django.shortcuts import render, Http404
from .models import *
from django.core.paginator import Paginator
import asyncio


# Create your views here.

def index(request):
    news = Actualité.objects.all()[:3]
    context = {'news': news}  
    return render(request, 'index.html', context)

def info(request):
    news = Actualité.objects.all()
    context = {'news': news}  
    return render(request, 'Actu/Actu.html', context)


def new_detail(request, pk):
    news = Actualité.objects.get(pk=pk)
    context = {'news': news}
    return render (request, 'Actu/Actu_view.html', context)

def scome(request):
    scome = Scome.objects.all()
    context = {'scome':scome}
    return render(request, 'comity/scome.html', context)

def scope(request):
    scope = Scope.objects.all()
    context = {'scope':scope}
    return render(request, 'comity/scope.html' , context)

def scoph(request):
    scoph = Scoph.objects.all()
    context = {'scoph':scoph}
    return render(request, 'comity/scoph.html' , context)

def score(request):
    score = Score.objects.all()
    context = {'score':score}
    return render(request, 'comity/score.html' , context)

def scorp(request):
    scorp = Scorp.objects.all()
    context = {'scorp':scorp}
    return render(request, 'comity/scorp.html', context)

def scora(request):
    scora = Scora.objects.all()
    context = {'scora':scora}
    return render(request, 'comity/scora.html', context)

def inscription(request):
    return render(request, 'inscription.html')
