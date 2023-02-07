from django import forms
from django.core import validators
class FormContact(forms.Form):
    name = forms.CharField(
        label = "Nombre",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tu nombre',
            }
        ),
        validators=[
            validators.MaxLengthValidator(25,'Verifica tu nombre, demasiado grande!'),
            validators.MinLengthValidator(3,'Verifica tu nombre, demasiado corto!'),
            validators.RegexValidator('[A-Za-z]','invalid_name')
        ]
    )

    lastName = forms.CharField(
        label = "Apellido",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tu apellido',
            }
        ),
        validators=[
            validators.MaxLengthValidator(30,'Verifica tu apellido, demasiado grande!'),
            validators.MinLengthValidator(3,'Verifica tu apellido, demasiado corto!'),
            validators.RegexValidator('[A-Za-z]','invalid_lastName')
        ]
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tu correo',
            }
        ),
        validators=[
            validators.MinLengthValidator(5,'Verifica bien tu correo'),
            validators.EmailValidator('Verifica tu correo!')
        ]
    )

    phone = forms.CharField(
        label="Telefono",
        required=True,
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Numero de contacto',
            }
        ),
        validators=[
            validators.MinLengthValidator(8,'Verifica bien tu numero telefonico'),
            validators.RegexValidator('[0-9]','invalid_phone')
        ]
    )

    description = forms.CharField(
        label = "Descripcion",
        required = True,
        max_length= 255,
        widget= forms.Textarea(
            attrs={
                'placeholder': '¿Cual es tu idea?'
            }            
        ),
        validators=[
            validators.MinLengthValidator(10,'se a detectado que no has escrito una descripcion coherencia.'),
            validators.RegexValidator('[^A-Za-z0-9ñ ]*$','invalid_description')
        ]
        
    )