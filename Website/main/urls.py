from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analysis', views.analysis, name='analysis'),
    path('about', views.about, name='about'),
]