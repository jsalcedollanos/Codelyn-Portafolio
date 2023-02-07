from django.shortcuts import render, HttpResponse, redirect
from portafolio.models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from portafolio.forms import FormContact 

def page(request, slug):

    lenguaje = {
        'Python': '<i class="bi bi-filetype-py"></i>',
        'Wordpress': '<i class="bi bi-wordpress"></i>',
        'PHP': '<i class="bi bi-filetype-php"></i>',
        'Laravel': 'Laravel',
        'JavaScript': 'Javascript',
        'CSS': '<i class="bi bi-filetype-css"></i>',
    }
    # Obtener proyectos  
    proyectos = Proyect.objects.all()
    # Paginar Proyectos
    paginator = Paginator(proyectos, 2)

    # Recoger numero pagina
    page = request.GET.get('page')
    page_proyectos = paginator.get_page(page)

    # Mostrar perfil
    perfiles = Perfil.objects.all()
    
    # Listar slugs (paginas)
    slugs = {
        'servicios':'servicios/',
        'portafolio':'portafolio/'
    }
    page = Page.objects.get(slug=slug)

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
            return redirect('/inicio/sobre-mi')
        else:
            formulario = FormContact()
            return render(request, 'page.html', {
            "form": formulario,
        })     
    return render(request, 'page.html', {
        "page": page,
        "proyectos": page_proyectos,        
        "lenguaje": lenguaje,
        "slugs":slugs,
        "cursos": cursos,
        "perfiles": perfiles,
        "servicios": servicios,
        "form": formulario,
    })
        
def crearContacto(request):
    
    formulario = FormContact() 
        
    return render(request, "crear-contacto.html", {
            'form':formulario
    })

