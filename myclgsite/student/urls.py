from django.urls import path
from . import views
urlpatterns = [
    path('', views.studenthome, name='studenthome'),
    path('dashboard/', views.studentdashboard, name='studentdashboard'),
    path('contact/', views.contact, name='contact'),
    path('academic/', views.academic, name='academic'),
    path('about/', views.about, name='about'),
    path('application/', views.application, name='application'),
    path('result/', views.result, name='result'),
    path('attendance/', views.bcaattendance, name='bcaattendance'),
    path('attendance/', views.bbaattendance, name='bbaattendance'),

]