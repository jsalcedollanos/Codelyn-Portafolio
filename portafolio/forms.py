from django import forms
from django.core import validators
class FormContact(forms.Form):
    name = forms.CharField(
        label = "Nombre"
    )

    lastName = forms.CharField(
        label = "Apellido"
    )

    email = forms.EmailField(
        label="Email"
    )

    phone = forms.IntegerField(
        label="Telefono"
    )

    description = forms.CharField(
        label = "Descripcion",
        widget= forms.Textarea(
            attrs={
                'placeholder': '¿Cual es tu idea?'
            }            
        ),
        validators=[
            validators.MinValueValidator(255, 'Solo se admiten 255 caracteres')
        ]
        
    )