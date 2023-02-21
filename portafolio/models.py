from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Proyect(models.Model):
    _id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    lenguage = models.CharField(max_length=200)
    status = models.BooleanField(default=True, verbose_name="estado")
    user = models.ForeignKey(User, verbose_name="Desarrollador", on_delete=models.CASCADE)
    image = models.ImageField(default='null', upload_to="proyect")
    progress = models.BooleanField(default=True, verbose_name="progreso")
    slug = models.URLField(null=True, blank=True, default="https://", max_length=200, verbose_name="Enlace")
    description = RichTextField(verbose_name="descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha actualizacion")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self) -> str:
        return f"{self.name} - {self.created_at}"

class Curso(models.Model):
    title = models.CharField(max_length=200, verbose_name = "titulo")
    description = models.TextField(max_length=200,verbose_name="descripcion")
    image = models.ImageField(default='null', upload_to="cursos")
    user = models.ForeignKey(User, verbose_name="Desarrollador", on_delete=models.CASCADE)
    status = models.BooleanField(default=True, verbose_name="estado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha actualizacion")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.title
    
class Contenido(models.Model):
    curso = models.ForeignKey(Curso, verbose_name="cursos", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, verbose_name = "titulo")
    description = RichTextField(verbose_name="descripcion")
    image = models.ImageField(default='null', upload_to="cursos")
    status = models.BooleanField(default=True, verbose_name="estado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha actualizacion")

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural = "Contenidos"

    def __str__(self):
        return self.title

class Clases(models.Model):
    curso = models.ForeignKey(Curso, default=1, verbose_name="curso", on_delete=models.CASCADE)
    contenido = models.ForeignKey(Contenido, verbose_name="contenido", on_delete=models.DO_NOTHING)
    title_class = models.CharField(max_length=200, verbose_name = "titulo clase")
    description = models.TextField(max_length=400, verbose_name="descripcion")
    url = models.URLField(null=True, blank=True, max_length=300, verbose_name="url video")
    status = models.BooleanField(default=True, verbose_name="estado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha actualizacion")

    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"

    def __str__(self):
        return self.title_class



class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name = "Nombre")
    description = RichTextField(verbose_name="descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha actualizacion")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=200 ,verbose_name="descripcion")
    content = RichTextField(verbose_name="contenido")
    image = models.ImageField(default='null', upload_to="articles")
    public = models.BooleanField(verbose_name="¿Publicado?")
    user = models.ForeignKey(User, verbose_name="usuario", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="categorias")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha actualizacion")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self) -> str:
        if self.public:
            public = "(publicado)"
        else:
            public = "(privado)"
        return f"{self.title}{public}"


class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="titulo")
    content = RichTextField(verbose_name="contenido")
    slug = models.CharField(unique=True, max_length=100, verbose_name="slug")
    visible = models.BooleanField(verbose_name="¿visible?")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Creado el")
    updated_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title

class Perfil(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre Completo")
    lastname = models.CharField(max_length=50, verbose_name="Apellidos")
    title = models.CharField(max_length=50, verbose_name="Titulo")
    email = models.EmailField(max_length=100, verbose_name="Correo")
    telephone = models.IntegerField()
    description = RichTextField(verbose_name="Descripcion")
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    skills = models.TextField(max_length=255, verbose_name="Habilidades") 
    image = models.ImageField(upload_to="perfil", verbose_name="Imagen perfil")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha actualizacion")

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=30, verbose_name="nombre")
    description = models.TextField(max_length=250, verbose_name="descipcion")
    subservices = RichTextField(verbose_name="sub-servicios")
    image = models.ImageField(default='null' ,upload_to="servicios", verbose_name="imagen")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha actualizacion")

    class meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=25, verbose_name="nombre")
    lastName = models.CharField(max_length=30, verbose_name="apellido")
    email = models.EmailField(max_length=50, verbose_name="correo")
    phone = models.CharField(max_length=12, verbose_name="telefono")
    description = models.TextField(max_length=255, verbose_name="descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha actualizacion")
    
    class meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.name


    