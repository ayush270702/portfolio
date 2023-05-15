from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('download/', views.download_resume, name='download_resume'),
]
