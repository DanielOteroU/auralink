# core/admin.py
from django.contrib import admin
from .models import Servicio, Contacto

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'mensaje') # Campos a mostrar en la lista

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')

# Register your models here.
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Contacto, ContactoAdmin)