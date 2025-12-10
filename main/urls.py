from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('certificates/', views.certificates, name='certificates'),
path('contact/', views.contact_view, name='contact'),
path('about/', views.about, name='about'),
]
