# Generated by Django 4.1.5 on 2023-05-18 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portafolio', '0065_perfil_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentClase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comentario')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha actualizacion')),
                ('classVideo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.clases', verbose_name='clase')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
        ),
    ]
