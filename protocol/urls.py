from django.urls import path
from . import views


urlpatterns = [
    path('protocol/', views.recherche, name='recherche'),
    path('<str:id>/', views.definition, name='definition'),
]    
