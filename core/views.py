from django.shortcuts import render, redirect
from .models import Servicio, Contacto
from django.contrib import messages
from .forms import ContactoForm  # Asegúrate de tener este archivo forms.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# Vista principal / inicio
def inicio(request):
    contexto = {
        'titulo': 'Impulsamos tu negocio con Inteligencia Artificial y soluciones digitales',
        'subtitulo': 'Conectamos ideas, potenciamos resultados.',
        'banner_img': 'core/wallpaper.png'
    }
    return render(request, 'core/inicio.html', contexto)

# Vista de servicios
def servicios(request):
    servicios = Servicio.objects.all()  # Trae todos los servicios desde la BD
    contexto = {
        'servicios': servicios
    }
    return render(request, 'core/servicios.html', contexto)

# Vista de contacto
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda directamente en la DB
            messages.success(request, '¡Tu mensaje ha sido enviado con éxito!')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor, completa todos los campos correctamente.')
    else:
        form = ContactoForm()
    
    contexto = {
        'form': form,
        'mensaje': 'Hablemos de cómo transformar tu negocio con Auralink'
    }
    return render(request, 'core/contacto.html', contexto)

# Vista para listar contactos
@login_required
def lista_contactos(request):
    contactos = Contacto.objects.all()  # Trae todos los contactos de la DB
    contexto = {
        'contactos': contactos
    }
    return render(request, 'core/lista_contactos.html', contexto)


def servicios_consumo_api(request):
    """Página que consumirá la API de servicios y mostrará los resultados via JS"""
    return render(request, 'core/servicios_api.html', {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            auth_login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido!')
            return redirect('inicio')
        else:
            messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
