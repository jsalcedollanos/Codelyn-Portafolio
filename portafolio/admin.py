from django.contrib import admin
from .models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
class ProyectAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
class PerfilAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

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
