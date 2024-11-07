from django.shortcuts import render
from .models import *
# Create your views here.

# def file(request):
#     if 'query' in request.GET:
#         query = request.GET['query']
#         drive = Media.objects.filter(title__icontains=query)
#     else:
#         drive = Media.objects.all()
#         return render(request, 'mediatheque/media.html', {'drive':drive})


def media(request):
    drive = Media.objects.all()
    return render(request, 'mediatheque/media.html', {'drive':drive})