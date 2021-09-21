from django.urls import path
from . import views
urlpatterns = [
    path('', views.teacherhome, name='teacherhome'),
    path('dashboard/', views.teacherdashboard, name='teacherdashboard'),
    path('academic/', views.academic, name='academic'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('application/', views.application, name='application'),
    path('attendance/', views.bcaattendance, name='bcaattendance'),
    path('attendance/', views.bbaattendance, name='bbaattendance'),


]