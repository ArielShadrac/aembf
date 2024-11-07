from django.shortcuts import render, Http404, HttpResponse
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def blog(request):
    if 'query' in request.GET:
        query = request.GET['query']
        posts = Article.objects.filter(title__icontains=query)
    else:
        posts = Article.objects.all()

    paginator = Paginator(posts, 10)
    posts = paginator.page(request.GET.get('page', 1))
    return render(request,'blog/blog.html', {'posts':posts})

def post_detail(request, id):
    try:
        posts = Article.objects.get(id=id)
        context = {'posts':posts}
    except posts.DoesNotExit:
        raise Http404('Page Non trouvé')
    return render(request,'blog/post_detail.html', context)
