# Generated by Django 4.1.5 on 2023-05-10 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0058_curso_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='user',
        ),
    ]
