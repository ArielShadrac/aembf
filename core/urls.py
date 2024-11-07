from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('scope/', views.scope, name='scope'),
    path('scoph/', views.scoph, name='scoph'),
    path('score/', views.score, name='score'),
    path('scorp/', views.scorp, name='scorp'),
    path('scora/', views.scora, name='scora'),
    path('scome/', views.scome, name='scome'),
    path('inscription/', views.inscription, name='inscription'),
    path('<int:pk>/', views.new_detail, name='new_detail'),

]
