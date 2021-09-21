from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('application', views.application, name='application'),
    path('about', views.about, name='about'),
    path('academic', views.academic, name='academic'),
    path('stulogin', views.stulogin, name='stulogin'),
    path('studentlogin', views.studentLogin, name="studentLogin"),
    path('teachlogin', views.teachLogin, name="teachLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('teacherlogin', views.teacherLogin, name="teacherLogin"),
    path('parlogin', views.parlogin, name='parlogin'),
    path('parentlogin', views.parentlogin, name="parentlogin"),
    path('bca', views.bca, name="bca"),
    path('bba', views.bba, name="bba"),
    path('mba', views.mba, name="mba"),
    path('pgdm', views.pgdm, name="pgdm"),
    path('mata', views.mata, name="mata"),

]