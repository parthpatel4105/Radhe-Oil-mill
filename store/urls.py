from django.urls import path

from . import views

urlpatterns = [
    path('', views.radhe_home, name='radhe_home'),
    path('contact/', views.contact, name='contact'),
]
