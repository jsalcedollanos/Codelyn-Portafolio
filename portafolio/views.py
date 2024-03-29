from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from portafolio.models import *
from django.core.paginator import Paginator
from django.contrib import messages
from portafolio.forms import *
from django.views.generic import (View, TemplateView, ListView, DetailView)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.serializers import serialize
from django.db.models import Avg, Count, Sum

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def handling_404(request, exception):
    return render(request, 'not-found-404.html', {

    })

def index(request):

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

    return render(request, 'index.html', {
        "page": page,
        "proyectos": page_proyectos,        
        "articulos": page_obj,
    })

def servicios(request):
    
    return render(request, 'servicios.html', {

    })

def cursos(request):

    # listar Cursos
    cursos = Curso.objects.all()

    # Añadir favorito
    formularioFa = FavoriteForm()

    if request.method == "POST":
        formularioFa = FavoriteForm(request.POST)
        if formularioFa.is_valid():
            data_form = formularioFa.cleaned_data
            curso = data_form.get('curso')

            favorito = Favorite(
                user_id = request.user.id,
                curso_id = curso,
            )
            favorito.save()
            messages.success(request, f'{request.user.first_name}, se ha agregado el curso a tu lista de favoritos!!!')
            
            return redirect('/explorar-cursos')
        else:
            messages.error(request,'No se pudo añadir a la lista...')

    return render(request, 'explorarCursos.html', {
        'cursos':cursos,
        'formularioFa':formularioFa,
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
    
    # añadir favorito
    formularioFa = FavoriteForm()
    if request.method == "POST":
        formularioFa = FavoriteForm(request.POST)
        if formularioFa.is_valid():
            data_form = formularioFa.cleaned_data
            curso = data_form.get('curso')

            favorito = Favorite(
                user_id = request.user.id,
                curso_id = curso,
            )
            favorito.save()
            messages.success(request, 'Se ha agregado el curso a tu lista de favoritos!!!')
            return redirect('/cursos')
        else:
            messages.error(request,'No se pudo añadir a la lista...')

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
        "formularioFa": formularioFa,
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

    
def handler404(request, exception):
    return render(request, '404.html')

def articulo(request, article_id):
    articulos = get_object_or_404(Article, id=article_id)
    comentarios = Comment.objects.filter(article_id = article_id)
    respuestas = CommentToComment.objects.all()
    ress = CommentToComment.objects.all()
    comm = Comment.objects.all()


    formRespuesta = FormRespuesta()
    if request.method == 'POST':
        formRespuesta = FormRespuesta(request.POST)
        if formRespuesta.is_valid():
            data_form = formRespuesta.cleaned_data
            respuesta = data_form.get('respuesta')
            resComentario = data_form.get('com')
            respuesta = CommentToComment(
                user = request.user,
                respuesta = respuesta,
                comment_id = resComentario,
            )

            respuesta.save()
            #Mensaje flash de successful
            messages.success(request, 'Tu Respuesta ha sido enviada con exito!')
            return redirect(f'/articulo/{article_id}')
        
    
    formComentario = FormComentario()
    if request.method == 'POST':
        formComentario = FormComentario(request.POST)
        if formComentario.is_valid():
            data_form = formComentario.cleaned_data
            com = data_form.get('comentario')
            com = Comment(
                comentario = com,
                user = request.user,
                article = articulos,
            )
            com.save()
            #Mensaje flash de successful
            messages.success(request, 'Tu comentario ha sido enviado con exito!')
            return redirect(f'/articulo/{article_id}')
        else:
            messages.error(request, '(Error al comentar) algo salio mal, revisa el formulario :D')
    
    return render(request, 'articulo.html', {
        'articulo':articulos,
        'comentarios':comentarios,
        'formComentario':formComentario,
        'formRespuesta':formRespuesta,
        'respuestas':respuestas,
        'ress':ress,
        'comm':comm,
    })


def curso_detail(request, curso_id):
    try:
        valor = ValorationCourse.objects.all().aggregate(promVal=Avg('valoracion'))
        contValoracion = ValorationCourse.objects.filter(curso=curso_id).count()
        # Cinco estrellas
        fiveStar = ValorationCourse.objects.filter(star=5).count()
        fivePorcent = fiveStar/contValoracion
        # Cuatro Estrellas
        fourStar = ValorationCourse.objects.filter(star=4).count()
        fourPorcent = fourStar/contValoracion
        # Tres Estrellas
        threeStar = ValorationCourse.objects.filter(star=3).count()
        threePorcent = threeStar/contValoracion
        # Dos Estrellas
        twoStar = ValorationCourse.objects.filter(star=2).count()
        twoPorcent = twoStar/contValoracion
        # Una Estrella
        oneStar = ValorationCourse.objects.filter(star=1).count()
        onePorcent = oneStar/contValoracion
    except ValorationCourse.DoesNotExist:
        valor = None
    
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
        'val':valor,
        'contenidos': contenidos,
        'clases':clases,
        'idClases':idClases,
        'canClases':canClases,
        'canContenido':canContenido,
        'contVal': contValoracion,
        
        #Diccionario de valoraciones --->
        'five': fiveStar, 'fivePorcent':fivePorcent,
        'four': fourStar, 'fourPorcent':fourPorcent,
        'three': threeStar, 'threePorcent':threePorcent,
        'two': twoStar,  'twoPorcent': twoPorcent,
        'one': oneStar, 'onePorcent':onePorcent,
    })


def clases_curso(request, curso_id, clase_id):
    cursos = get_object_or_404(Curso, id=curso_id)
    contenidos = Contenido.objects.all()
    idClases = Clases.objects.values_list('id','contenido')
    commentClase = CommentClase.objects.filter(classVideo_id=clase_id)
    clases = Clases.objects.filter(curso=curso_id)
    className = Clases.objects.get(id=clase_id)
    canClases = Clases.objects.filter(curso=curso_id).count()
    canContenido = Contenido.objects.filter(curso_id=curso_id).count()
    perfilId = request.user.id
    perfil = Perfil.objects.get(user_id=perfilId)

    respuestas = ResComClase.objects.all()
    contResp = ResComClase.objects.get(id=clase_id)


    # FORMULARIO DE RESPUESTA
    formRespuestaClase = FormResClass()
    if request.method == 'POST':
        formRespuestaClase = FormResClass(request.POST)
        if formRespuestaClase.is_valid():
            data_form = formRespuestaClase.cleaned_data
            res = data_form.get('respuesta')
            com = data_form.get('comentario')
            res = ResComClase(
                respuesta = res,
                comment_id = com,
                perfil = perfil,
            )
            res.save()
            return redirect(f'/curso/{curso_id}/{clase_id}')
            

    # FORMULARIO DE COMENTARIO
    formComentarioClase = FormComentarioClase()
    if request.method == 'POST':
        formComentarioClase = FormComentarioClase(request.POST)
        if formComentarioClase.is_valid():
            data_form = formComentarioClase.cleaned_data
            com = data_form.get('comentario')
            com = CommentClase(
                comment = com,
                classVideo = className,
                perfil = perfil
            )
            com.save()
            #Mensaje flash de successful
            messages.success(request, f'{request.user.username} tu comentario ha sido enviado con exito!')
            return redirect(f'/curso/{curso_id}/{clase_id}')
        else:
            messages.error(request, '(Error al comentar) algo salio mal, revisa el formulario :D')

    return render(request, 'clases.html', {
        'contResp':contResp,
        'respuestas':respuestas,
        'formComentarioClase':formComentarioClase,
        'formRespuestaClase':formRespuestaClase,
        'className':className,
        'clase':clases,
        'commentClases':commentClase,
        'curso':cursos,
        'contenidos': contenidos,
        'clases':clases,
        'idClases':idClases,
        'canClases':canClases,
        'canContenido':canContenido,
    })

def delete_commentClase(request, id):
    commentClase = CommentClase.objects.get(id=id)
    commentClase.delete()
    pre_url = request.META.get('HTTP_REFERER') # Here
    return redirect(pre_url)

def delete_respuesta(request, id):
    respuestaComent = ResComClase.objects.get(id=id)
    respuestaComent.delete()
    pre_url = request.META.get('HTTP_REFERER') # Here
    return redirect(pre_url)

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
        'register_form': register_form,
        'title': 'Registrate'
    })

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Algo salio mal, revisa bien los datos ingresados.')

    return render(request, 'users/login.html',{
        'title': 'Identificate',
    })

def logout_user(request):
    logout(request)
    return redirect('/')


def commentClass(request, id):
    commentClase = CommentClase.objects.filter(id=id)
    return render(request, 'clases.html', {
        'commentClases':commentClase
    })
