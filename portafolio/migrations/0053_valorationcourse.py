# Generated by Django 4.1.5 on 2023-05-07 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portafolio', '0052_remove_page_meta_title_page_metatitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValorationCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='valoracion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha actualizacion')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.curso', verbose_name='curso')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'Valoracion',
                'verbose_name_plural': 'Valoracion',
            },
        ),
    ]
