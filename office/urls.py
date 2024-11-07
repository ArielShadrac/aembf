from django.urls import path
from . import views

urlpatterns = [
    path('BN/', views.national, name='BN'),
    path('UJKZ/', views.ujkz , name='UJKZ'),
    path('USTA/', views.usta , name='USTA'),
    path('INSSA/', views.inssa , name='INSSA'),
    path('UOHG/', views.uohg , name='UOHG'),
    path('USDAO/', views.usdao, name='USDAO'),
]