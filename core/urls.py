# core/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('servicios-api/', views.servicios_consumo_api, name='servicios_api'),
    path('contacto/', views.contacto, name='contacto'),
    path('register/', views.register, name='register'),
    path('lista_contactos/', views.lista_contactos, name='lista_contactos'),
    # API routes
    path('api/', include('core.api_urls')),
    # Auth (login/logout) using django contrib
    path('accounts/', include('django.contrib.auth.urls')),
]