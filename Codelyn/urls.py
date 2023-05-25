"""Codelyn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Datos estaticos
from django.contrib import admin
from django.urls import path
from portafolio import views
from django.conf import settings
from django.conf.urls import handler404



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name="index"),
    path('servicios/', views.servicios, name="servicios"),
    path('explorar-cursos/', views.cursos, name="cursos"),
    path('articulo/<int:article_id>', views.articulo, name="articulo"),
    path('curso/<int:curso_id>', views.curso_detail, name="curso_detail"),
    path('comentario/<int:id>', views.delete_commentClase, name="deleteComment"),
    path('respuesta/<int:id>', views.delete_respuesta, name="deleteRes"),
    path('curso/<int:curso_id>/<int:clase_id>', views.clases_curso, name="clases"),
    path('registro/', views.register_page, name="registro"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
]

#handler404 = Error404View.as_view()
handler404 = 'portafolio.views.handler404'

# Configurar titulo de panel admin
admin.site.site_header = "Codelyn"
admin.site.site_title = "Codelyn"
admin.site.index_title = "Panel de gestion"


# CONFIGURACION PARA CARGAR IMAGENES

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)