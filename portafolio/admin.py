from django.contrib import admin
from .models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content') # Añadir un buscador a mi listado
    list_filter = ('public',) # Añadir filtro a mi listado
    list_display = ('title','public','created_at') # Añadir campos en mi listado
    ordering = ('created_at',) # Ordenar listado desde el campo 'created_at'
class ProyectAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'lenguage', 'description') # Añadir un buscador a mi listado
    list_filter = ('progress',) # Añadir filtro a mi listado
    list_display = ('name','lenguage','user','progress','created_at') # Añadir campos en mi listado
    ordering = ('created_at',) # Ordenar listado desde el campo 'created_at'
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # Colocar campos solo visibles
    search_fields = ('title', 'content') # Añadir un buscador a mi listado
    list_filter = ('visible',) # Añadir filtro a mi listado
    list_display = ('title','visible','created_at') # Añadir campos en mi listado
    ordering = ('created_at',) # Ordenar listado desde el campo 'created_at'
class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'description') # Añadir un buscador a mi listado
    list_filter = ('status',) # Añadir filtro a mi listado
    list_display = ('title','status','user','created_at') # Añadir campos en mi listado
    ordering = ('created_at',) # Ordenar listado desde el campo 'created_at'
class PerfilAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name','lastname') # Añadir un buscador a mi listado
    list_display = ('name','lastname','title','email','telephone','skills','created_at') # Añadir campos en mi listado
    ordering = ('created_at',) # Ordenar listado desde el campo 'created_at'
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name','created_at')
    ordering = ('created_at',)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name','lastName','email','phone','created_at')
    ordering = ('created_at',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Proyect, ProyectAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Contact, ContactAdmin)

# Configurar titulo de panel admin
admin.site.site_header = "Codelyn"
admin.site.site_title = "Codelyn"
admin.site.index_title = "Panel de gestion"



