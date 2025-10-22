from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(
        max_length=100,
        min_length=3,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Tu nombre',
            'class': 'form-control',
            'minlength': 3,
            'maxlength': 100,
            'required': True
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'correo@ejemplo.com',
            'class': 'form-control',
            'required': True
        })
    )
    mensaje = forms.CharField(
        min_length=10,
        max_length=500,
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Escribe tu mensaje aquí',
            'class': 'form-control',
            'rows': 5,
            'minlength': 10,
            'maxlength': 500,
            'required': True
        })
    )
    empresa = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Tu empresa',
            'class': 'form-control',
        })
    )
    telefono = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Tu teléfono',
            'class': 'form-control',
            'pattern': r'^\+?\d{7,20}$',  # solo números y opcional +
            'title': 'Solo números, mínimo 7 y máximo 20 dígitos'
        })
    )

    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje', 'empresa', 'telefono']
