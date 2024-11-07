from django.urls import path
from . import views

urlpatterns = [
    path('Blog/', views.blog, name='blog'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]
