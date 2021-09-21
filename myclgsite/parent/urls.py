from django.urls import path
from . import views
urlpatterns = [
    path('', views.parenthome, name='parenthome'),
    path('contact/', views.contact, name='contact'),
    path('academic/', views.academic, name='academic'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.parentdashboard, name='parentdashboard'),
    path('application/', views.application, name='application'),
    path('result/', views.result, name='result'),
]