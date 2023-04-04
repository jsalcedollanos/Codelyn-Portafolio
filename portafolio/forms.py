from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1','password2']

class FormComentario(forms.Form):
    comentario = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Escribe tu comentario...',
            }
        ),
        validators=[
            validators.MaxLengthValidator(300,'Texto demasiado largo, Maximo 300 caracteres.'),
            validators.MinLengthValidator(2,'Verifica tu comentario, esta muy corto'),
        ]
    )

class FormRespuesta(forms.Form):
    respuesta = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Responde algo aqui..',
            }
        ),
        validators=[
            validators.MaxLengthValidator(300,'Texto demasiado largo, Maximo 300 caracteres.'),
            validators.MinLengthValidator(2,'Verifica tu comentario, esta muy corto'),
        ]
    )

    com = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'id':'comentarioP',
                'class':'comentarioP'
            }
        ),
        
    )



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