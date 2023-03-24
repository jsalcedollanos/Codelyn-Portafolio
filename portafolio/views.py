from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from portafolio.models import *
from django.core.paginator import Paginator
from django.contrib import messages
from portafolio.forms import FormContact, RegisterForm, FormComentario
from django.views.generic import (View, TemplateView, ListView, DetailView)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def handling_404(request, exception):
    return render(request, 'not-found-404.html', {

    })


def page(request, slug):

     

    lenguaje = {
        'Python': '<i class="bi bi-filetype-py"></i>',
        'Wordpress': '<i class="bi bi-wordpress"></i>',
        'PHP': '<i class="bi bi-filetype-php"></i>',
        'Laravel': 'Laravel',
        'JavaScript': 'Javascript',
        'CSS': '<i class="bi bi-filetype-css"></i>',
    }


    # Articulos
    articulos = Article.objects.all()
    # Paginar Articulos
    paginator_articulos = Paginator(articulos, 5)
    # Recoger numero pagina
    page_number = request.GET.get('page')
    page_obj = paginator_articulos.get_page(page_number)


    # Obtener proyectos  
    proyectos = Proyect.objects.all()
    # Paginar Proyectos
    paginator = Paginator(proyectos, 2)

    # Recoger numero pagina
    page = request.GET.get('page')
    page_proyectos = paginator.get_page(page)

    # Mostrar perfil
    perfiles = Perfil.objects.all()

    #pages = Page.objects.get(slug)
    if slug == slug:
        #Listar slugs
        page = Page.objects.get(slug=slug)    
    else:
        return render(request, '404.html') 
    
    
    # listar Cursos
    cursos = Curso.objects.all()

    # Listar servicios
    servicios = Service.objects.all()

    # formulario
    formulario = FormContact()
    if request.method == "POST":
        formulario = FormContact(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            name = data_form.get('name')
            lastName = data_form.get('lastName')
            email = data_form.get('email')
            phone = data_form.get('phone')
            description = data_form.get('description')

            contacto = Contact(
                name = name,
                lastName = lastName,
                email = email,
                phone = phone,
                description = description,
            )

            contacto.save()
            #Mensaje flash de successful
            messages.success(request, f'Perfecto {contacto.name} en breve te contactare para charlar mejor!')
            return redirect('/sobre-mi')
        else:
            messages.error(request, 'Uy... Espera algo salio mal, revisa el formulario :D')
        
    
    return render(request, 'page.html', {
        "page": page,
        "proyectos": page_proyectos,        
        "lenguaje": lenguaje,
        "articulos": page_obj,
        "cursos": cursos,
        "perfiles": perfiles,
        "servicios": servicios,
        "form": formulario,
    })
        

def redes(request):
    sociales = Perfil.objects.all()
    return render(request, 'layout.html', {
        'sociales':sociales
    })

""" class Error404View(TemplateView):
    templante_name = "404.html" """
    
def handler404(request, exception):
    return render(request, '404.html')

def articulo(request, article_id):
    articulos = get_object_or_404(Article, id=article_id)
    comentarios = Comment.objects.filter(article_id = article_id)

    formComentario = FormComentario()
    if request.method == "POST":
        formComentario = FormComentario(request.POST)
        if formComentario.is_valid():
            data_form = formComentario.cleaned_data
            comentario = data_form.get('comentario')
            #user = data_form.get('user')
            article = data_form.get('article')

            comentario = Comment(
                comentario = comentario,
                user = request.user,
                article = articulos,
            )

            comentario.save()
            #Mensaje flash de successful
            messages.success(request, 'Tu comentario ha sido enviado con exito!')
            return redirect(f'/articulo/{article_id}')
        else:
            messages.error(request, 'Uy... Espera algo salio mal, revisa el formulario :D')

    return render(request, 'articulo.html', {
        'articulo':articulos,
        'comentarios':comentarios,
        'formComentario':formComentario,
    })

def curso_detail(request, curso_id):
    cursos = get_object_or_404(Curso, id=curso_id)
    contenidos = Contenido.objects.filter(curso=curso_id)
    #idContenido = Contenido.objects
    idClases = Clases.objects.values_list('id','contenido')
    clases = Clases.objects.filter(curso=curso_id)
    canClases = Clases.objects.filter(curso=curso_id).count()
    canContenido = Contenido.objects.filter(curso_id=curso_id).count()
    #idClase = get_object_or_404(Clases, id)
    return render(request, 'curso_detail.html', {
        'curso':cursos,
        'contenidos': contenidos,
        'clases':clases,
        'idClases':idClases,
        'canClases':canClases,
        'canContenido':canContenido,
    })

def clase_curso(request, curso_id, clase_id):
    cursos = get_object_or_404(Curso, id=curso_id)
    claseId = get_object_or_404(Clases, id=clase_id)
    contenidos = Contenido.objects.all()
    clases = Clases.objects.all()
    canClases = Clases.objects.all().count()
    canContenido = Contenido.objects.all().count()
    return render(request, 'clase_detail.html', {
        'clase':clases,
        'claseId':claseId,
        'curso':cursos,
        'contenidos': contenidos,
        'clases':clases,
        'canClases':canClases,
        'canContenido':canContenido,
    })

def register_page(request):

    register_form = RegisterForm()

    if request.method == 'POST':
       register_form = RegisterForm(request.POST) 

       if register_form.is_valid():
           register_form.save()
           messages.success(request, f'Perfecto has creado tu cuenta con exito! BIENVENIDO =D')
          
       else:
           messages.error(request, 'Error al guardar tu informacion, revisa porfavor!')

    return render(request, 'users/register.html', {
        'register_form': register_form
    })

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/inicio')
        else:
            messages.error(request, 'Algo salio mal, revisa bien los datos ingresados.')

    return render(request, 'users/login.html',{
        'title': 'Identificate',
    })

def logout_user(request):
    logout(request)
    return redirect('/inicio')




