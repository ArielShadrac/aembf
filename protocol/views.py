from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def recherche(request):
    if 'word' in request.GET:
        word = request.GET['word']
        search = Protocol.objects.filter(nom__icontains=word)
    else:
        search = Protocol.objects.all()
    context = {'search':search}
    return render(request, 'protocol/protocol.html', context)

def definition(request,id):
    search = Protocol.objects.get(id=id)
    context = {'search':search}
    return render(request, 'protocol/protocol_view.html', context)


#========================================Paginator=======================================#

# def mot(request):
#     mots = Mot.objects.all()
#     paginator = Paginator(mots, 2)
#     mots = paginator.page(request.GET.get('page', 1))
#     return render(request, 'dictionnaire/dictionnaire.html', {'mots':mots})

#========================================Paginator=======================================#